from blog.models import (Folder, Post, MCQ, Category, MCQTag, MCQIssue, Path)
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.serializers import (
	ModelSerializer,ReadOnlyField, ValidationError,CharField, IntegerField )
from rest_framework.exceptions import PermissionDenied


class FolderSerializer(ModelSerializer):
	category = CharField(max_length=10)
	distance = IntegerField()
	class Meta:
		model = Folder
		fields = ['name', 'distance','category' ,'root_loc']

	def __init__(self, *args, **kwargs):
		instance = kwargs.pop('instance', None)
		super(FolderSerializer, self).__init__(*args, **kwargs)
		if instance:
			self.instance = instance


	def validate_category(self, value):
		try:
			category = Category.objects.get(name__iexact=value)
			return category
		except ObjectDoesNotExist as e:
			raise ValidationError("category doesn't exists")


	def _validate_paths(self, self_loc, root_loc):
		if self_loc.uid == root_loc.uid:
			raise ValidationError("invalid parent selected")
		return


	def validate(self, data):
		if self.instance:
			if data.get('root_loc',None):
				self._validate_paths(self.instance.self_loc, data.get('root_loc'))
		return data


	def create(self, validated_data):
		folder = Folder.objects.create(
			name=validated_data.get('name'),
			distance=validated_data.get('distance'),
			category=validated_data.get('category'),
			root_loc=validated_data.get('root_loc'),
			self_loc=Path.objects.create()
			)
		return folder


	def update(self, validated_data):
		self.instance.name = validated_data.get('name')
		self.instance.distance = validated_data.get('distance')
		self.instance.category = validated_data.get('category')
		if validated_data.get('root_loc', None):
			self.instance.root_loc = validated_data.get('root_loc')
		self.instance.save()
		return self.instance



class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title','body', 'folder', 'entry_by']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		instance = kwargs.pop('instance', None)
		super(PostSerializer, self).__init__(*args, **kwargs)
		self.user = user
		if instance:
			self.instance = instance

	def validate(self, data):
		if self.user != data.get('entry_by'):
			raise ValidationError({"entry_by":"invalid user"})
		return data



	def create(self, validated_data):
		post = Post.objects.create(
			title=validated_data.get('title'),
			body=validated_data.get('body'),
			entry_by=validated_data.get('entry_by'),
			folder=validated_data.get('folder')
			)
		return post


	def update(self, validated_data):
		self.instance.title = validated_data.get('title')
		self.instance.body = validated_data.get('body')
		self.instance.folder = validated_data.get('folder')
		self.instance.entry_by = validated_data.get('entry_by')
		self.instance.save()
		return self.instance



class MCQSerializer(ModelSerializer):
	class Meta:
		model = MCQ
		fields = ['question', 'option1', 'option2', 'option3',
				'option4', 'answer', 'summary', 'level', 'entry_by']



class MCQTagSerializer(ModelSerializer):
	class Meta:
		model = MCQTag
		fields = ['mcq', 'folder']



class MCQIssueSerializer(ModelSerializer):
	class Meta:
		model = MCQIssue
		fields = ['mcq','body']


	def __init__(self, *args, **kwargs):
		user = kwargs.pop("user")
		super(MCQIssueSerializer, self).__init__(*args, **kwargs)
		self.user = user


	def validate(self, data):
		return data


	def create(self, validated_data):
		mcq_issue = MCQIssue.objects.create(
			user=self.user,
			mcq=validated_data.get('mcq'),
			body=validated_data.get('body')
		)
		return mcq_issue
