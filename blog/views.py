from django.shortcuts import render

# Create your views here.

from blog.graph.engine import Query, Mutation
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
		name = request.POST.get('name', None)
		if name is None:
			raise ValidationError('name must be provided')
		category_name = request.POST.get('categoryName', None)
		if category_name is None:
			raise ValidationError('category must be provided')
		distance = request.POST.get('distance', None)
		if distance is None:
			raise ValidationError('distance must be provided')
		rootLoc_uid = request.POST.get('rootLocUid', None)
		result = Mutation.create_folder(name,category_name,distance, rootLoc_uid)
		return HttpResponse(result, content_type='application/json')


class CreatePost(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		title = request.POST.get('title', None)
		if title is None:
			raise ValidationError('title must be provided')
		body = request.POST.get('body',None)
		if body is None:
			raise ValidationError('body must be provided')
		folder_loc = request.POST.get('folderLoc', None)
		if folder_loc is None:
			raise ValidationError('folder location must be provided')
		result = Mutation.create_post(title, body, folder_loc)
		return HttpResponse(result, content_type='application/json')



class CreateMCQ(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		ques = request.POST.get('question', None)
		if ques is None:
			raise ValidationError('ques must be provided')

		op1 = request.POST.get('option1', None)
		if op1 is None:
			raise ValidationError('option1 must be provided')

		op2 = request.POST.get('option2', None)
		if op2 is None:
			raise ValidationError('option2 must be provided')

		op3 = request.POST.get('option3', None)
		if op3 is None:
			raise ValidationError('option3 must be provided')

		op4 = request.POST.get('option4', None)
		if op4 is None:
			raise ValidationError('option4 must be provided')

		ans = request.POST.get('answer', None)
		if ans is None:
			raise ValidationError('answer must be provided')

		summary = request.POST.get('summary', None)
		if summary is None:
			raise ValidationError('summary must be provided')

		level = request.POST.get('level', None)
		if level is None:
			raise ValidationError('level must be provided')

		result = Mutation.create_mcq(ques,op1,op2,op3,op4,ans,summary,level)
		return HttpResponse(result, content_type='application/json')