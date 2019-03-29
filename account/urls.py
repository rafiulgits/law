from account.views import auth

from django.urls import path
from django.contrib.auth import views as resetviews

urlpatterns = [
	
	path('signup/', auth.signup, name='signup'),
	path('signin/', auth.signin, name='signin'),
	path('signout/', auth.signout, name='signout'),


	path('password-reset/', resetviews.PasswordResetView.as_view(
		template_name='account/password/reset.html'),name='password_reset'),

    path('password-reset/done/', resetviews.PasswordResetDoneView.as_view(
    	template_name='account/password/reset-done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', resetviews.PasswordResetConfirmView.as_view(
    	template_name='account/password/reset-confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', resetviews.PasswordResetCompleteView.as_view(
    	template_name='account/password/reset-complete.html'), name='password_reset_complete'),

]