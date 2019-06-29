from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetviews

urlpatterns = [

	path('signup/', auth.SignUp.as_view(), name='signup'),
	path('signin/', auth.SignIn.as_view(), name='signin'),
	path('signout/', auth.SignOut.as_view(), name='signout'),
	path('profile/', manage.Profile.as_view(), name='user-profile'),
]