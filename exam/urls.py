from django.urls import path
from exam import views


urlpatterns = [
	path('mcq/', views.MCQExam.as_view(), name='mcq-exam'),
	path('public-mcq-exams/', views.PublicExamList.as_view(), name='public-exam-list'),
]