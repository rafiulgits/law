from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetviews
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('signup/', auth.SignUp.as_view(), name='signup'),
	path('signin/', auth.SignIn.as_view(), name='signin'),
	path('access-renew/', TokenRefreshView.as_view(), name='access-renew'),
	path('profile/', manage.Profile.as_view(), name='user-profile'),
]