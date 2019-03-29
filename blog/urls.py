from django.urls import path,include

from blog.views import manage

urlpatterns = [
	path('', manage.index , name='blog-index')
]