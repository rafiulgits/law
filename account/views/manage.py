from account.forms import ProfileUpdateForm
from account.serializers import ProfileSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


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