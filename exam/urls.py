from django.urls import path
from exam import views


urlpatterns = [
	path('create-mcq-exam/', views.CreateMCQExam.as_view()),
	path('create-clone-mcq-exam/', views.CreateCloneMCQExam.as_view()),
	path('create-mcq-exam-item/', views.CreateMCQExamItem.as_view()),
	path('create-omr/', views.CreateOMR.as_view()),
	path('public-mcq-exams/', views.PublicMCQExams.as_view()),
	path('mcq-exam/<uid>/', views.MCQExam.as_view()),
	path('user-exam-list/', views.UserMCQExams.as_view()),
]