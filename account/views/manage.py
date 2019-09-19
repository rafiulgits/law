from account.forms import ProfileUpdateForm
from account.graph.engine import Query
from account.serializers import ProfileSerializer

from django.shortcuts import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Profile(APIView):
	permission_classes = (IsAuthenticated,)
	renderer_classes = (JSONRenderer,)

	def get(self, request, format=None):
		result = Query.profile(request.user.id)
		return HttpResponse(result, content_type='application/json')


	def post(self, request, format=None):
		serializer = ProfileSerializer(request.POST)
		serializer.set_current_user(request.user)
		if serializer.is_valid():
			profile = serializer.create(serializer.validated_data)
			result = Query.profile(profile.account.id)
			return HttpResponse(result, content_type='application/json')
		return HttpResponse(serializer.errors, status=400)