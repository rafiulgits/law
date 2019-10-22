from exam import models
from graphene_django.types import DjangoObjectType
from graphene import relay


class MCQExamSourceType(DjangoObjectType):
	class Meta:
		model = models.MCQExamSource
		filter_fields = '__all__'
		interfaces = (relay.Node,)



class MCQExamItemType(DjangoObjectType):
	class Meta:
		model = models.MCQExamItem
		filter_fields = '__all__'
		interfaces = (relay.Node,)



class MCQExamType(DjangoObjectType):
	class Meta:
		model = models.MCQExam
		filter_fields = '__all__'
		interfaces = (relay.Node,)



class MCQReportType(DjangoObjectType):
	class Meta:
		model = models.MCQReport
		filter_fields = '__all__'
		interfaces = (relay.Node,)



class OMRType(DjangoObjectType):
	class Meta:
		model = models.OMR
		filter_fields = '__all__'
		interfaces = (relay.Node,)
