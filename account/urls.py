from django.urls import path
from django.contrib.auth import views as resetviews

urlpatterns = [
	
	path('password-reset/', resetviews.PasswordResetView.as_view(
		template_name='account/auth/password-reset.html'),name='password_reset'),

    path('password-reset/done/', resetviews.PasswordResetDoneView.as_view(
    	template_name='account/auth/password-reset-done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', resetviews.PasswordResetConfirmView.as_view(
    	template_name='account/auth/password-reset-confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', resetviews.PasswordResetCompleteView.as_view(
    	template_name='account/auth/password-reset-complete.html'), name='password_reset_complete'),

]