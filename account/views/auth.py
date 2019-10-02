from account.serializers import (ProfileSerializer,LogSerializer,
AccountSerializer, AccountUpdateSerializer, PasswordChangeSerializer)
from account.models import Account

from django.shortcuts import redirect

from rest_framework.exceptions import NotFound,NotAcceptable,ValidationError
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
			return Response('{"res": "ok"}')
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
