from django.urls import path,include

from blog import views
urlpatterns = [
	path('subjects/', views.AllSubjects.as_view()),
	path('folder/', views.FolderManager.as_view()),
	path('post/', views.PostManager.as_view()),
	path('mcq-create/', views.CreateMCQ.as_view()),
	path('mcq-tag/', views.MCQTagManager.as_view()),
	path('mcq-list/', views.MCQList.as_view()),
	path('mcq-issue/create/', views.MCQIssueCreate.as_view()),
	path('mcq-issue/<int:uid>/', views.MCQIssueManager.as_view())
]