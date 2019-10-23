from blog.models import (Folder, Post, MCQ, Category, MCQTag, MCQIssue)
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

	def validate_category(self, value):
		try:
			Category.objects.get(name__iexact=value)
			return value
		except ObjectDoesNotExist as e:
			raise ValidationError("category doesn't exists")


class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title','body', 'folder', 'entry_by']



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
