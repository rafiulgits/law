from django.shortcuts import HttpResponse

from exam.serializers import *
from exam.graph.engine import Mutation, Query

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError



class CreateMCQExam(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		serializer = MCQExamSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_mcq_exam(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)
		



class CreateCloneMCQExam(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		serializer = MCQExamCloneSerializer(data=request.POST)
		if serializer.is_valid():	
			result = Mutation.create_clone_mcq_exam(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


class CreateMCQExamItem(APIView):

	permission_classes = (IsAuthenticated, )

	def post(self, request, format=None):
		serializer = MCQExamItemSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_mcq_exam_item(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


class CreateOMR(APIView):

	permission_classes = (IsAuthenticated, )

	def post(self, request, format=None):
		serializer = OMRSerializer(data=request.POST)
		if serializer.is_valid():
			result = Mutation.create_omr(serializer.validated_data)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


class AllMCQExams(APIView):

	def get(self, request, format=None):
		result = Query.all_mcq_exams()
		return HttpResponse(result, content_type='application/json')