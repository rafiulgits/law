from django.urls import path,include

from blog import views
urlpatterns = [
	path('subjects/', views.all_subjects, name='all_subjects'),
	path('folder/', views.explore_folder, name='explore_folder'),
	path('post/<uid>/', views.single_post, name='single_post'),
]