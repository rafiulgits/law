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
		fields = ['user','mcq','body']


	def set_current_user(self, user):
		self.current_user = user


	def validate(self, data):
		user = data.get('user')
		if user != self.current_user:
			raise PermissionDenied("access denied")
		return data


	def create(self, validated_data):
		mcq_issue = MCQIssue.objects.create(
			user=validated_data.get('user'),
			mcq=validated_data.get('mcq'),
			body=validated_data.get('body')
		)
		return mcq_issue