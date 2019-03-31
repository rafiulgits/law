from account.forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from generic.variables import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def profile(request):
	context = {}
	return render(request, 'account/manage/profile.html', context)


@login_required(login_url=LOGIN_URL)
def update(request):
	context = {}
	form = ProfileUpdateForm(user=request.user)
	context['form'] = form
	return render(request, 'account/manage/update.html', context)

