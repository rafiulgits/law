from django.urls import path

from cpanel import views

urlpatterns = [
	path('dashboard/', views.Dashboard.as_view()),
	path('support/', views.SupportBoxView.as_view()),
	path('allusers/<int:page>/', views.AllUsers.as_view()),
	path('allissues/', views.AllIssues.as_view()),
]