from account.forms import ProfileUpdateForm
from account.serializers import ProfileSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from generic.const import LOGIN_URL

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Profile(APIView):
	permission_classe = (IsAuthenticated,)
	renderer_classes = (JSONRenderer,)

	def get(self, request, format=None):
		serializer = ProfileSerializer(request.user)
		return Response(serializer.data)


	def post(self, request, format=None):
		pass


	def put(self, request, format=None):
		pass



@login_required(login_url=LOGIN_URL)
def profile(request):
	context = {}
	return render(request, 'account/manage/profile.html', context)


@login_required(login_url=LOGIN_URL)
def update(request):
	context = {}
	form = ProfileUpdateForm(user=request.user)
	context['form'] = form
	return render(request, 'account/manage/update.html', context)

