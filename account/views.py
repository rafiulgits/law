from django.shortcuts import render

from account.forms import SigninForm

# Create your views here.


def check(request):
	context = {}

	form = SigninForm()
	context['form'] = form
	context['v'] = 100
	return render(request, 'account/auth/signin.html', context)