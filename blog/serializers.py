from blog.models import Folder, Post, MCQ, Category
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import (
	ModelSerializer,ReadOnlyField, ValidationError,CharField, IntegerField )

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
		fields = ['title','body', 'folder']


class MCQSerializer(ModelSerializer):
	class Meta:
		model = MCQ
		fields = ['question', 'option1', 'option2', 'option3',
				'option4', 'answer', 'summary', 'level']