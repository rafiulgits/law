from django.urls import path,include

from blog import views
urlpatterns = [
	path('subjects/', views.AllSubjects.as_view(), name='all_subjects'),
	path('folder/', views.ExploreFolder.as_view(), name='explore_folder'),
	path('post/<uid>/', views.SinglePost.as_view(), name='single_post'),

	path('addfolder/', views.CreateFolder.as_view(), name='create-folder'),
	path('addpost/', views.CreatePost.as_view(), name='create-post'),
	path('addmcq/', views.CreateMCQ.as_view(), name='create-mcq'),
]