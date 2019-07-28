from django.shortcuts import render

# Create your views here.

from blog.api.engine import Query
from django.shortcuts import HttpResponse
from rest_framework.exceptions import NotFound

def all_subjects(request):
	result = Query.all_subjects()
	return HttpResponse(result, content_type='application/json')


def explore_folder(request):
	location = request.GET.get('location', None)
	if location is None:
		raise NotFound('location have to be provided')
	result = Query.explore_folder(location)
	return HttpResponse(result, content_type='application/json')


def single_post(request, uid):
	result = Query.get_post(uid)
	return HttpResponse(result, content_type='application/json')