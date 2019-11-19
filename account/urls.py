from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetviews
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('signup/', auth.SignUp.as_view()),
	path('signin/', auth.SignIn.as_view()),
	path('access-renew/', TokenRefreshView.as_view()),
	path('profile/', manage.Profile.as_view()),
	path('update/', auth.AccountUpdate.as_view()),
	path('password-change/', auth.PasswordChange.as_view()),
	path('verify/', auth.VerifyEmail.as_view()),

	path('password-reset/request/', auth.PasswordResetRequest.as_view()),
	path('password-reset/verify/', auth.VerifyPasswordRequest.as_view()),
	path('password-reset/', auth.PasswordResetView.as_view()),
]