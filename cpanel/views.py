from account.models import Account
from exam.models import MCQExam
from blog.models import MCQIssue
from rest_framework.views import APIView
from rest_framework.response import Response



class Dashboard(APIView):
    def get(self, request):
        total_account = Account.objects.all().count()
        total_exam = MCQExam.objects.all().count()
        pending_issues = MCQIssue.objects.filter(is_solved=False).count()

        result = {
            'totalAccount' : total_account,
            'totalExam' : total_exam,
            'pendingIssues' : pending_issues
        }

        return Response(result)
