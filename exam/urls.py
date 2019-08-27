from django.urls import path
from exam import views


urlpatterns = [
	path('create-mcq-exam/', views.CreateMCQExam.as_view()),
	path('create-clone-mcq-exam/', views.CreateCloneMCQExam.as_view()),
	path('create-mcq-exam-item/', views.CreateMCQExamItem.as_view()),
	path('create-omr/', views.CreateOMR.as_view()),
	path('all-mcq-exams/', views.AllMCQExams.as_view())
]