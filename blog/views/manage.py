from blog.models import Folder

from django.shortcuts import render

def index(request):
	return render(request,'blog/index.html', {})



def subjects(request):
	context = {}
	query = "SELECT * FROM blog_folder WHERE UPPER(category_id)=UPPER('Subject')"
	result = Folder.objects.raw(query)

	context['result'] = result
	return render(request, 'blog/manage/subjects.html', context)