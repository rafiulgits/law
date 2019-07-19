from account.forms import SignupForm, SigninForm
from account.serializers import ProfileSerializer

from django.contrib.auth import login, logout
from django.shortcuts import redirect

from rest_framework.exceptions import NotFound,NotAcceptable
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class SignIn(APIView):
	renderer_classes = (JSONRenderer,)

	def post(self, request, format=None):
		form = SigninForm(request.POST)
		if form.is_valid():
			user = form.user
			login(request, user)
			serializer = ProfileSerializer(user)
			return Response({
				'user' : serializer.data,
				'token' : Token.objects.get(user=user).key
			})
		else:
			raise NotFound({
				'errors' : form.errors
			})


class SignUp(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, format=None):
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			serializer = ProfileSerializer(user)
			return Response({
				'user' : serializer.data,
				'token' : Token.objects.create(user=user).key
			})
		else:
			raise NotAcceptable({
				'errors' : form.errors
			})



class SignOut(APIView):
	renderer_classes = (JSONRenderer,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		logout(request)
		return redirect('/')