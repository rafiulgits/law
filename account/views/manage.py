from account.graph.engine import Query
from account.serializers import ProfileSerializer, ProfileUpdateSerializer
from account.models import Profile as ProfileModel

from django.shortcuts import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Profile(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		result = Query.profile(request.user.id)
		return HttpResponse(result, content_type='application/json')


	def post(self, request, format=None):
		serializer = ProfileSerializer(data=request.POST)
		serializer.set_current_user(request.user)
		if serializer.is_valid():
			profile = serializer.create(serializer.validated_data)
			result = Query.profile(profile.account.id)
			return HttpResponse(result, content_type='application/json')
		return HttpResponse(serializer.errors, status=400)


	def put(self, request, format=None):
		profile = ProfileModel.objects.get(account=request.user)
		serializer = ProfileUpdateSerializer(
			profile=profile, 
			account=request.user, 
			data=request.POST)
		if serializer.is_valid():
			profile = serializer.update(serializer.validated_data)
			result = Query.profile(profile.account.id)
			return HttpResponse(result, content_type='application/json')
		else:
			raise HttpResponse(serializer.errors, content_type='application/json', status=400)