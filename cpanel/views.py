from account.models import Account
from blog.models import MCQIssue
from cpanel.graph.engine import Query
from cpanel.serializer import SupportBoxSerializer
from django.shortcuts import HttpResponse
from exam.models import MCQExam
from generic.permissions import IsStaffUser
from rest_framework.exceptions import ValidationError
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






class SupportBoxView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		serializer = SupportBoxSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse({"message":"OK"}, content_type='application/json')
		raise ValidationError(serializer.errors)
