from draft import models
from graphene_django.types import DjangoObjectType
from graphene import relay


class ArticleType(DjangoObjectType):
	class Meta:
		model = models.Article
		filter_fields = {
			'uid' : ['exact'],
			'title' : ['exact', 'icontains'],
		}
		interfaces = (relay.Node,)