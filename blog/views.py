from blog.graph.engine import Query
from blog.models import Category, MCQIssue, Post, Folder
from blog.serializers import (PostSerializer, FolderSerializer, MCQSerializer, 
	MCQTagSerializer, MCQIssueSerializer)
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from generic.permissions import IsStaffUser

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError,PermissionDenied
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
		result = Query.explore_folder(rootLoc=location)
		return HttpResponse(result, content_type='application/json')

	def post(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		serializer = FolderSerializer(data=request.POST)
		if serializer.is_valid():
			folder = serializer.create(serializer.validated_data)
			result = Query.explore_folder(rootLocUid=folder.self_loc_id)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


	def put(self, request):
		if not request.user.is_staff:
			PermissionDenied("access denied")
		self_loc_uid = request.GET.get('self_loc_uid', None)
		if not self_loc_uid:
			raise ValidationError('folder self location required')
		try:
			folder = Folder.objects.get(self_loc_id=self_loc_uid)
			serializer = FolderSerializer(data=request.POST, instance=folder)
			if serializer.is_valid():
				folder = serializer.update(serializer.validated_data)
				result = Query.explore_folder(rootLocUid=folder.self_loc_id)
				return HttpResponse(result, content_type='application/json')
		except ObjectDoesNotExist:
			raise NotFound({"folder":"invalid folder UID"})


	def delete(self, request):
		if not request.user.is_staff:
			PermissionDenied("access denied")
		self_loc_uid = request.GET.get('self_loc_uid', None)
		if not self_loc_uid:
			raise ValidationError('folder self location required')
		try:
			folder = Folder.objects.get(self_loc_id=self_loc_uid)
			result = Query.explore_folder(rootLocUid=folder.self_loc_id)
			folder.delete()
			return HttpResponse(result, content_type='application/json')
		except ObjectDoesNotExist:
			raise NotFound({"folder":"folder against this UID not found"})





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
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		serializer = PostSerializer(data=request.POST, user=request.user)
		if serializer.is_valid():
			post = serializer.create(serializer.validated_data)
			result = Query.get_post(post.uid)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


	def put(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		uid = request.GET.get('uid', None)
		if not uid:
			raise NotFound("post uid is required")
		try:
			post = Post.objects.get(uid=uid)
			serializer = PostSerializer(data=request.POST,
				instance=post,user=request.user)
			if serializer.is_valid():
				post = serializer.update(serializer.validated_data)
				result = Query.get_post(post.uid)
				return HttpResponse(result, content_type='application/json')
			raise ValidationError(serializer.errors)
		except ObjectDoesNotExist:
			raise NotFound("invalid post uid")


	def delete(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		uid = request.GET.get('uid', None)
		if not uid:
			raise NotFound("post uid is required")
		try:
			post = Post.objects.get(uid=uid)
			result = Query.get_post(post.uid)
			post.delete()
			return HttpResponse(result, content_type='application/json')
		except ObjectDoesNotExist:
			raise NotFound("post not found")




class CreateMCQ(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		if not request.user.is_staff:
			PermissionDenied("access denied")
		serializer = MCQSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.mcq(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)



class MCQList(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		if request.GET.get('after', None):
			result = Query.mcq_list(after=request.GET.get('after'))
		elif request.GET.get('before', None):
			result = Query.mcq_list(before=request.GET.get('before'))
		else:
			result = Query.mcq_list()
		return HttpResponse(result, content_type='application/json')




class MCQTagManager(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		if not request.user.is_staff:
			PermissionDenied("access denied")
		serializer = MCQTagSerializer(data=request.POST)
		if serializer.is_valid():
			result = Create.mcq_tag(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


	def delete(self, request):
		if not request.user.is_staff:
			PermissionDenied("access denied")
		if request.POST.get('mcq_tag_uid', None) is None:
			raise ValidationError('mcq tag uid is required')
		result = Delete.mcq_tag(request.POST)
		return HttpResponse(result, content_type='application/json')




class MCQIssueCreate(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		serializer = MCQIssueSerializer(data=request.POST,user=request.user)
		if serializer.is_valid():
			mcq_issue = serializer.create(serializer.validated_data)
			return HttpResponse('{"response": "ok"}', content_type='application/json')
		return HttpResponse(serializer.errors, status=400)




class MCQIssueManager(APIView):

	permission_classes = (IsAuthenticated, IsStaffUser)

	def get(self, request, uid):
		result = Query.get_issue(uid)
		return HttpResponse(result, content_type='application/json')


	def put(self, request, uid):
		try:
			issue = MCQIssue.objects.get(uid=uid)
			if not issue.is_solved:
				issue.is_solved = True
				issue.save()
			result = Query.get_issue(issue.uid)
			return HttpResponse(result, content_type='application/json')
		except ObjectDoesNotExist:
			raise NotFound("issue not found")
