from blog.models import (Category, Path, Folder, Post, MCQ, CQ)

from django import forms

from generic.variables import random


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','body']

		widgets = {
			'title' : forms.TextInput(attrs={}),
			'body' : forms.TextInput(attrs={})
		}


	def save(self, commit=True):
		post = super(PostForm, self).save(commit=False)

		if self.post is None:
			post.uid = random()
			post.folder = self.folder

		if commit:
			post.save()

		return post

	def __init__(self, *args, **kwargs):
		self.folder = kwargs.pop('folder', None)
		self.post = kwargs.pop('post', None)
		super(PostForm, self).__init__(*args, **kwargs)

		if post is not None:
			self.fields['title'].initial = self.post.title
			self.fields['body'].initial = self.post.body


class MCQForm(forms.ModelForm):
	class Meta:
		model = MCQ
		fields = ['question','option1','option2','option3','option4','answer']


		widgets = {
			'question' : forms.TextInput(attrs={}),
			'option1' : forms.TextInput(attrs={}),
			'option2' : forms.TextInput(attrs={}),
			'option3' : forms.TextInput(attrs={}),
			'option4' : forms.TextInput(attrs={}),
			'answer' : forms.NumberInput(attrs={})
		}


	def save(self, commit=True):
		mcq = super(MCQForm,self).save(commit=False)

		if self.mcq is None:
			mcq.uid = random()
			mcq.folder = self.folder

		if commit:
			mcq.save()

		return mcq


	def __init__(self, *args, **kwargs):
		self.folder = kwargs.pop('folder', None)
		self.mcq = kwargs.pop('mcq', None)
		super(MCQForm, self).__init__(*args, **kwargs)

		if self.mcq is not None:
			self.fields['question'].initial = self.mcq.question
			self.fields['option1'].initial = self.mcq.option1
			self.fields['option2'].initial = self.mcq.option2
			self.fields['option3'].initial = self.mcq.option3
			self.fields['option4'].initial = self.mcq.option4
			self.fields['answer'].initial = self.mcq.answer


class CQCForm(forms.ModelForm):
	class Meta:
		model = CQ
		fields = ['question']

		widgets = {
			'question' : forms.TextInput(attrs={})
		}


	def save(self):
		cq = super(CQForm, self).save(commit=False)

		if self.cq is None:
			cq.uid = random()
			cq.folder = self.folder

		if commit:
			cq.save()
		return cq


	def __init__(self, *args, **kwargs):
		self.folder = kwargs.pop('folder', None)
		self.cq = kwargs.pop('cq', None)
		super(CQForm, self).__init__(*args, **kwargs)

		if cq is not None:
			self.fields['question'].initial = self.cq.question

