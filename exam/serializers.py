from exam import models
from rest_framework.serializers import (ModelSerializer, CharField)


class MCQExamSerializer(ModelSerializer):
	class Meta:
		model = models.MCQExam
		fields = ['name','level','marks','total_mcq','public','created_by']



class MCQExamItemSerializer(ModelSerializer):
	class Meta:
		model = models.MCQExamItem
		fields = ['mcq','exam']


class MCQExamCloneSerializer(ModelSerializer):
	class Meta:
		model = models.MCQExamClone
		fields = ['name','origin','cloned_by']


class OMRSerializer(ModelSerializer):
	class Meta:
		model = models.OMR
		fields = ['mcq','answer','report']
