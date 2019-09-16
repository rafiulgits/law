from blog.graph.engine import Query, Create, Update, Delete
from blog.serializers import (PostSerializer, FolderSerializer, MCQSerializer, 
	MCQTagSerializer)
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from blog.models import Category

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated



class AllSubjects(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		result = Query.all_subjects()
		return HttpResponse(result, content_type='application/json')



class FolderManager(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		location = request.GET.get('location', None)
		if location is None:
			raise NotFound('location have to be provided')
		result = Query.explore_folder(location)
		return HttpResponse(result, content_type='application/json')

	def post(self, request):
		serializer = FolderSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.folder(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)

	def delete(self, request):
		if request.POST.get('self_loc_uid', None) is None:
			raise ValidationError('folder self location required')
		result = Delete.folder(request.POST)
		return HttpResponse(result, content_type='application/json')





class PostManager(APIView):

	permission_classes = (IsAuthenticated,)

	def get(self, request):
		uid = request.GET.get('uid', None)
		if uid is None:
			raise ValidationError('post uid required')
		else:
			result = Query.get_post(uid)
			return HttpResponse(result, content_type='application/json')

	def post(self, request):
		serializer = PostSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.post(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)

	def delete(self, request):
		if request.POST.get('post_uid', None) is None:
			raise ValidationError('post UID required')
		result = Delete.post(request.POST)
		return HttpResponse(result, content_type='application/json')




class CreateMCQ(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = MCQSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.mcq(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)



class MCQList(APIView):
	def get(self, request):
		if request.GET.get('after', None):
			result = Query.mcq_list(after=request.GET.get('after'))
		elif request.GET.get('before', None):
			result = Query.mcq_list(before=request.GET.get('before'))
		else:
			result = Query.mcq_list()
		return HttpResponse(result, content_type='application/json')



class MCQTagManager(APIView):

	def post(self, request):
		serializer = MCQTagSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.mcq_tag(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


	def delete(self, request):
		if request.POST.get('mcq_tag_uid', None) is None:
			raise ValidationError('mcq tag uid is required')
		result = Delete.mcq_tag(request.POST)
		return HttpResponse(result, content_type='application/json')
