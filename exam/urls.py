from django.urls import path
from exam import views


urlpatterns = [
	path('mcq/', views.MCQExam.as_view(), name='mcq-exam'),
	path('public-mcq-exams/', views.PublicExamList.as_view(), name='public-exam-list'),
	path('mcq/report/', views.MCQReport.as_view(), name='mcq-exam-report'),
	path('mcq/mylist/', views.UserExamList.as_view(), name='user-mcq-exam-list'),
]