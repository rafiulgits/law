from account.forms import ProfileUpdateForm
from account.serializers import ProfileSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from generic.const import LOGIN_URL

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound 


class Profile(APIView):
	permission_classes = (IsAuthenticated,)
	renderer_classes = (JSONRenderer,)

	def get(self, request, format=None):
		serializer = ProfileSerializer(request.user)
		return Response(serializer.data)


	def post(self, request, format=None):
		pass


	def put(self, request, format=None):
		pass