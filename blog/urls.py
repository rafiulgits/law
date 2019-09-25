from django.urls import path,include

from blog import views
urlpatterns = [
	path('subjects/', views.AllSubjects.as_view(), name='all-subjects'),
	path('folder/', views.FolderManager.as_view(), name='folder-manager'),
	path('post/', views.PostManager.as_view(), name='post-manager'),
	path('mcq-create/', views.CreateMCQ.as_view(), name='mcq-create'),
	path('mcq-tag/', views.MCQTagManager.as_view(), name='mcq-tag-manager'),
	path('mcq-list/', views.MCQList.as_view(), name='mcq-list'),
	path('mcq-issue/', views.MCQIssueManager.as_view(), name='mcq-issue-manager'),
]