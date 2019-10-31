from django.urls import path
from exam import views


urlpatterns = [
	path('mcq/', views.MCQExam.as_view()),
	path('mcq/sheet/<int:uid>/', views.MCQExamSheet.as_view()),
	path('public-mcq-exams/', views.PublicExamList.as_view()),
	path('mcq/report/', views.MCQReport.as_view()),
	path('mcq/mylist/', views.UserExamList.as_view()),
]