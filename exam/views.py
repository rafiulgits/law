from django.shortcuts import HttpResponse

from exam.serializers import (MCQExamSerializer, MCQExamCloneSerializer, ReportGeneratorSerializer)
from exam.graph.engine import  Query

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


class PublicExamList(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		result = Query.all_mcq_exams()
		return HttpResponse(result, content_type='application/json')



class MCQExam(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		"""
		GET request is for retrieve an exam information
		"""
		uid = request.GET.get('uid', None)
		if uid is None:
			raise ValidationError("exam UID must be provided")
		result = Query.mcq_exam(uid)
		return HttpResponse(result, content_type='application/json')


	def post(self, request):
		"""
		POST request is for create a new exam
		"""
		serializer = MCQExamSerializer(data=request.POST)
		serializer.set_current_user(request.user)
		if serializer.is_valid():
			exam = serializer.create(serializer.validated_data)
			result = Query.mcq_exam(exam.uid)
			return HttpResponse(result, content_type='application/json')
		return HttpResponse(serializer.errors, status=400)


	def put(self, request):
		"""
		PUT request is for clone an existing mcq exam
		"""
		serializer = MCQExamCloneSerializer(data=request.POST)
		serializer.set_current_user(request.user)
		if serializer.is_valid():
			exam = serializer.create(serializer.validated_data)
			result = Query.mcq_exam(exam.uid)
			return HttpResponse(result, content_type='application/json')
		else:
			print("Invalid")
			print(serializer.errors)
		return HttpResponse(serializer.errors, status=400)




class MCQReport(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = ReportGeneratorSerializer(data=request.data)
		serializer.set_current_user(request.user)
		if serializer.is_valid():
			exam = serializer.create(serializer.validated_data)
			result = Query.mcq_exam_report(exam.uid)
			return HttpResponse(result, content_type='application/json')
		return HttpResponse(serializer.errors, status=400)