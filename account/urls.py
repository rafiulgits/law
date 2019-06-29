from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetviews

urlpatterns = [

	path('', manage.profile, name='profile'),
	path('update/', manage.update, name='profile-update'),
	
	path('signup/', auth.SignUp.as_view(), name='signup'),
	path('signin/', auth.SignIn.as_view(), name='signin'),
	path('signout/', auth.SignOut.as_view(), name='signout'),


	path('profile/', manage.Profile.as_view(), name='user-profile'),


	path('password-reset/', resetviews.PasswordResetView.as_view(
		template_name='account/password/reset.html'),name='password_reset'),

    path('password-reset/done/', resetviews.PasswordResetDoneView.as_view(
    	template_name='account/password/reset-done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', resetviews.PasswordResetConfirmView.as_view(
    	template_name='account/password/reset-confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', resetviews.PasswordResetCompleteView.as_view(
    	template_name='account/password/reset-complete.html'), name='password_reset_complete'),

]