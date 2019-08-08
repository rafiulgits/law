from blog.graph.engine import Query, Mutation
from blog.serializers import PostSerializer, FolderSerializer, MCQSerializer
from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated



class AllSubjects(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		result = Query.all_subjects()
		return HttpResponse(result, content_type='application/json')


class ExploreFolder(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		location = request.GET.get('location', None)
		if location is None:
			raise NotFound('location have to be provided')
		result = Query.explore_folder(location)
		return HttpResponse(result, content_type='application/json')


class SinglePost(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, uid):
		result = Query.get_post(uid)
		return HttpResponse(result, content_type='application/json')


class CreateFolder(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = FolderSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_folder(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


class CreatePost(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = PostSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_post(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


class CreateMCQ(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = MCQSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_mcq(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)