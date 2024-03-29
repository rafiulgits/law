from account.models import Account
from blog.models import MCQIssue, MCQ
from cpanel.graph.engine import Query
from cpanel.models import SupportBox
from cpanel.serializer import SupportBoxSerializer, MCQSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse
from exam.models import MCQExam
from generic.permissions import IsStaffUser
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class Dashboard(APIView):
	permission_classes = (IsAuthenticated, IsStaffUser)

	def get(self, request):
		total_account = Account.objects.all().count()
		total_exam = MCQExam.objects.all().count()
		total_pending_issue = MCQIssue.objects.filter(is_solved=False).count()
		result = {
			'totalAccount' : total_account,
			'totalExam' : total_exam,
			'totalPendingIssue' : total_pending_issue 
		}
		return Response(result)



class AllUsers(APIView):
	permission_classes = (IsAuthenticated, IsStaffUser)

	def get(self, request, page):
		result = Query.all_users(page)
		return HttpResponse(result, content_type='application/json')



class AllIssues(APIView):
	permission_classes = (IsAuthenticated, IsStaffUser)

	def get(self, request):
		result = Query.all_issues()
		return HttpResponse(result, content_type='application/json')



class AllSupportMessage(APIView):
	permission_classes = (IsAuthenticated, IsStaffUser)

	def get(self, request, page):
		if page:
			if page > 0:
				offset = (page-1)*50
				result = SupportBox.objects.all().order_by('-date_time')[offset:offset+50]
				serializer = SupportBoxSerializer(result, many=True)
				return Response(serializer.data)
		result = SupportBox.objects.all().order_by('-date_time')[0:50]
		serializer = SupportBoxSerializer(result, many=True)
		return Response(serializer.data)



class SupportBoxView(APIView):
	def post(self, request):
		serializer = SupportBoxSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse({"message":"OK"}, content_type='application/json')
		raise ValidationError(serializer.errors)





class MCQManager(APIView):
	
	permission_classes = (IsAuthenticated, IsStaffUser,)

	def get(self, request, uid):
		result = Query.get_mcq(uid)
		return HttpResponse(result, content_type='application/json')


	def put(self, request, uid):
		try:
			instance = MCQ.objects.get(uid=uid)
			serializer = MCQSerializer(data=request.POST, instance=instance)
			if serializer.is_valid():
				instance = serializer.save()
				return HttpResponse({"res" : "OK"}, content_type='application/json')
			else:
				raise ValidationError(serializer.errors);
		except ObjectDoesNotExist:
			raise NotFound("item not found")