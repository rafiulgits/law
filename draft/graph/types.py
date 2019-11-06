from draft import models
from graphene_django.types import DjangoObjectType
from graphene import relay



class PointerType(DjangoObjectType):
	class Meta:
		model = models.Pointer
		filter_fields = ['uid']
		interfaces = (relay.Node,)


class DirectoryType(DjangoObjectType):
	class Meta:
		model = models.Directory
		filter_fields = {
			'name' : ['exact', 'icontains', 'istartswith'],
			'self_loc' : ['exact'],
			'self_loc__uid' : ['exact'],
			'root_loc': ['exact'],
			'root_loc__uid': ['exact']
		}
		interfaces = (relay.Node, )



class ArticleType(DjangoObjectType):
	class Meta:
		model = models.Article