from blog.models import Folder, Path, Category, _CATEGORIES_LIST

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse

from generic.variables import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def create(request):
	if request.method != 'POST':
		return redirect(request.path_info)
	if not request.user.has_perm('blog.can_add_folder'):
		return HttpResponse("You don't have permission")

	root_uid = request.GET.get('root', None)
	name = request.GET.get('name', None)
	category_name = request.GET.get('category', None)

	if name or category_name is None:
		return redirect(request.path_info)

	try:

		category_name = category_name.lower()
		for item in _CATEGORIES_LIST:
			if item.lower() != category_name:
				return redirect(request.path_info)

		try:
			category = Category.objects.get(name__iexact=category_name)
		except ObjectDoesNotExist as e:
			category = Category.objects.create(name=category_name.capitalize())

		if root_uid is None:
			folder = Folder(name=name, category=category, url_path='/'+name+'/')
			folder.save()

		else:
			try:
				root = Path.objects.get(uid=root_uid)
				root_folder = Folder.get(node=root)

				folder = Folder(name=name, category=category, root=root)
				folder.distance = root_folder.distance+1
				folder.url_path = root_folder.url_path+name+'/'
				folder.save()

			except ObjectDoesNotExist as e:
				pass

	except ObjectDoesNotExist as e:
		pass
	return redirect(request.path_info)
	

# 	