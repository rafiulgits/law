from blog import models
from graphene_django.types import DjangoObjectType
from graphene import relay


class CategoryType(DjangoObjectType):
	class Meta:
		model = models.Category
		filter_fields = {
			'uid' : ['exact'],
			'name' : ['exact', 'icontains']
		}
		interfaces = (relay.Node,)



class PathType(DjangoObjectType):
	class Meta:
		model = models.Path
		filter_fields = ['uid']
		interfaces = (relay.Node,)


class FolderType(DjangoObjectType):
	class Meta:
		model = models.Folder
		filter_fields = {
			'name' : ['exact', 'icontains', 'istartswith'],
			'distance' : ['exact'],
			'category' : ['exact'],
			'category__name' : ['exact', 'icontains'],
			'self_loc' : ['exact'],
			'root_loc': ['exact']
		}
		interfaces = (relay.Node, )


class PostType(DjangoObjectType):
	class Meta:
		model = models.Post


class MCQType(DjangoObjectType):
	class Meta:
		model = models.MCQ
		filter_fields = {}
		interfaces = (relay.Node, )



class MCQTagType(DjangoObjectType):
	class Meta:
		model = models.MCQTag
		filter_fields = {
			'folder' : ['exact'],
		}
		interfaces = (relay.Node,)


class MCQLabelType(DjangoObjectType):
	class Meta:
		model = models.MCQLabel
		filter_fields = {
			'name' : ['exact', 'icontains'],
		}
		interfaces = (relay.Node,)




class CQType(DjangoObjectType):
	class Meta:
		model = models.CQ




class CQTagType(DjangoObjectType):
	class Meta:
		model = models.CQTag
		filter_fields = {
			'folder' : ['exact']
		}
		interfaces = (relay.Node,)



class MCQIssueType(DjangoObjectType):
	class Meta:
		model = models.MCQIssue
		filter_fields = {
			'uid' : ['exact'],
			'user__id' : ['exact'],
			'mcq__uid' : ['exact'],
			'is_solved' : ['exact']
		}
		interfaces = (relay.Node,)
