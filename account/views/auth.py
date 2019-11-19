from account.serializers import (ProfileSerializer,LogSerializer,
AccountSerializer, AccountUpdateSerializer, PasswordChangeSerializer,
PasswordResetRequestSerializer, ResetRequestVerifySerializer,PasswordResetSerializer)
from account.models import Account, Reset

from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import NotFound,NotAcceptable,ValidationError, MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from generic.service import verify_email,decode


def _get_user_token(user):
	token = RefreshToken.for_user(user)
	data = {
		'refresh' : str(token),
		'access' : str(token.access_token)
	}
	return data


class SignIn(APIView):
	renderer_classes = (JSONRenderer,)

	def post(self, request, format=None):
		serializer = LogSerializer(data=request.POST)
		if serializer.is_valid():
			user = serializer.get_user()
			data = _get_user_token(user)
			return Response(data)
		else:
			raise ValidationError(serializer.errors)


class SignUp(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, format=None):
		serializer = AccountSerializer(data=request.POST)
		if serializer.is_valid():
			user = serializer.create(serializer.validated_data)
			if not user.is_active:
				verify_email(user)
				return Response({"res":"waiting for verification"})
			else:
				data = _get_user_token(user)
				return Response(data)
		else:
			raise ValidationError(serializer.errors)


class VerifyEmail(APIView):
	renderer_classes = (JSONRenderer,)
	def get(self, request, token):
		data = decode(token)
		if data:
			account = Account.objects.get(id=data['user_id'])
			if not account.is_active:
				account.is_active = True
				account.save()
				return redirect('https://askriashad.com/login')
		raise NotAcceptable("invalid request")


class AccountUpdate(APIView):
	permission_classes = (IsAuthenticated,)

	def put(self, request):
		serializer = AccountUpdateSerializer(account=request.user, data=request.POST)
		if serializer.is_valid():
			account = serializer.save(serializer.validated_data, True)
			return Response({"res": "ok"})
		else:
			raise ValidationError(serializer.errors)


class PasswordChange(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		serializer = PasswordChangeSerializer(account=request.user, data=request.POST)
		if serializer.is_valid():
			user = serializer.save(serializer.validated_data)
			data = _get_user_token(user)
			return Response(data)
		else:
			raise ValidationError(serializer.errors)




from generic.service import generate_token, verify_token, send_template_mail


class PasswordResetRequest(APIView):
	def post(self, request):
		serializer = PasswordResetRequestSerializer(data=request.POST)
		if not serializer.is_valid():
			raise ValidationError(serializer.errors)
		try:
			account = Account.objects.get(email__iexact=serializer.validated_data['email'])
			reset_object, created = Reset.objects.get_or_create(account=account)
			raw_data = {'uid' : str(reset_object.uid)}
			token = generate_token(raw_data, expired_days=1)
			context = {
				'token' : token, 'name' : account.name, 'date_time' : reset_object.date_time,
				'url' : 'https://askriashad.com/password-reset/?token={}'.format(token)
			}
			send_template_mail(to_mail=account.email,subject='AksRiashad Password Reset', 
				body_path='password_reset/request.txt',template_path='password_reset/request.html',
				context=context)
			if not created:
				reset_object.save()
			return Response({'request' : 'OK'})
		except ObjectDoesNotExist:
			raise ValidationError({"email" : "no account found with this email address"})




class VerifyPasswordRequest(APIView):

	def post(self, request):
		serializer = ResetRequestVerifySerializer(data=request.POST)
		if not serializer.is_valid():
			raise ValidationError(serializer.errors)
		data = verify_token(serializer.validated_data['token'])
		if not data:
			raise ValidationError({"token" : "invalid token"})
		try:
			reset_object = Reset.objects.get(uid=data['uid'])
			tokens = _get_user_token(reset_object.account)
			reset_object.delete()
			return Response(tokens)
		except ObjectDoesNotExist:
			raise ValidationError({"token" : "this token is not workable anymore"})




class PasswordResetView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = PasswordResetSerializer(data=request.POST, user=request.user)
		if serializer.is_valid():
			user = serializer.update(serializer.validated_data)
			return Response({'RES' : 'OK' })
		raise ValidationError(serializer.errors)
