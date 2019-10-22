from django.core.exceptions import ObjectDoesNotExist

from draft.graph.types import ArticleType
from draft.models import Article

from graphene_django.filter import DjangoFilterConnectionField
import graphene



class Query(graphene.ObjectType):
	article = graphene.Field(ArticleType, uid=graphene.ID())
	all_article = DjangoFilterConnectionField(ArticleType)
    
	def resolve_article(self, info, **kwargs):
		uid = kwargs.get('uid', None)
		if uid is None:
			raise ValueError('you must provide uid')
		try:
			obj = Article.objects.get(uid=uid)
			return obj
		except ObjectDoesNotExist:
			raise ValueError('must provide an valid uid')

