from account.serializers import (ProfileSerializer,LogSerializer,
AccountSerializer)

from rest_framework.exceptions import NotFound,NotAcceptable
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView


class SignIn(APIView):
	renderer_classes = (JSONRenderer,)

	def post(self, request, format=None):
		serializer = LogSerializer(data=request.POST)
		if serializer.is_valid():
			user = serializer.get_user()
			token = RefreshToken.for_user(user)
			data = {
				'refresh' : str(token),
				'access' : str(token.access_token)
			}
			return Response(data)
		else:
			print(serializer.errors)
			raise NotFound({'errors':'Authentication failed'})


class SignUp(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, format=None):
		serializer = AccountSerializer(data=request.POST)
		if serializer.is_valid():
			user = serializer.create(serializer.validated_data)
			token = RefreshToken.for_user(user)
			data = {
				'refresh' : str(token),
				'access' : str(token.access_token)
			}
			return Response(data)
		else:
			print(serializer.errors)
			raise NotAcceptable({
				'errors' : "failed"
			})
