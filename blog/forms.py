from blog.models import (Category, CQ, CQTag, Folder, MCQ, MCQTag,Path, Post)

from django import forms


class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields =['name','category','root']


	def save(self, commit=True):
		name = self.cleaned_data['name']
		category = self.cleaned_data['category']
		root = self.cleaned_data['root']

		folder = Folder(name=name, root=root, category=category)
		folder.node = Path()
		if root is not None:
			folder.distance = root.distance+1

		if commit:
			folder.save()
		return folder




class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'folder']

	def save(self, commit=True):
		post = super(PostForm, self).save(commit=commit)
		return post




class MCQForm(forms.ModelForm):
	path = forms.IntegerField(forms.NumberInput())
	class Meta:
		model = MCQ
		fields =[
			'question', 
			'option1',
			'option2',
			'option3',
			'option4',
			'answer',
			'summary'
		]

	def save(self, commit=True):
		mcq = super(MCQForm, self).commit(commit=False)
		path_uid = self.cleaned_data['path']

		# Access path then folder
		# folder = Folder.objects.get(path_uid=path_uid)
		if folder.distance == 0:
			pass
			# single tag
		else:
			pass
			# loop taging

		if commit:
			# save all tags
			post.save()
		return post



class CQForm(forms.ModelForm):
	path = forms.IntegerField(forms.NumberInput())
	class Meta:
		model = CQ
		fields = ['question']


	def save(self, commit=True):
		path_uid = self.cleaned_data['path']
		folder = Folder.objects.get(node_id=path_uid)

		# complete the taging
		
		cq = super(CQForm, self).save(commit=False)
		if commit:
			cq.save()