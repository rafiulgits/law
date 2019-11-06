from django.core.exceptions import ObjectDoesNotExist

from draft.graph import types
from draft.models import (Pointer, Directory, Article)
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from graphql_relay.node.node import from_global_id


class Query(graphene.ObjectType):
	pointer = graphene.relay.Node.Field(types.PointerType)
	all_pointers = DjangoFilterConnectionField(types.PointerType)

	directory = graphene.Field(types.DirectoryType, self_loc=graphene.String(), 
			self_loc_uid=graphene.String())
	all_directories = DjangoFilterConnectionField(types.DirectoryType)

	article = graphene.Field(types.ArticleType, uid=graphene.ID())
	all_article = graphene.List(types.ArticleType)
    


	def resolve_directory(self, info, **kwargs):
		self_loc_uid = kwargs.get('self_loc_uid', None)
		if self_loc_uid:
			try:
				return Directory.objects.get(self_loc=self_loc_uid)
			except ObjectDoesNotExist:
				return None
		self_loc = kwargs.get('self_loc', None)
		if self_loc:
			try:
				uid = from_global_id(self_loc)[1]
				return Directory.objects.get(self_loc_id=uid)
			except Exception:
				pass
		return None


	def resolve_all_directories(self, info, **kwargs):
		self_loc_uid = kwargs.get('self_loc__uid', None)
		root_loc_uid = kwargs.get('root_loc__uid', None)
		if self_loc_uid:
			return Directory.objects.filter(self_loc_id=self_loc_uid)
		elif root_loc_uid:
			return Directory.objects.filter(root_loc_id=root_loc_uid)
		root_loc = kwargs.get('root_loc', None)
		if root_loc:
			if root_loc.lower() == 'null':
				return Directory.objects.filter(root_loc=None)
		return Directory.objects.all()


	def resolve_article(self, info, **kwargs):
		uid = kwargs.get('uid', None)
		if uid is None:
			raise ValueError('you must provide uid')
		try:
			obj = Article.objects.get(uid=uid)
			return obj
		except ObjectDoesNotExist:
			raise ValueError('must provide an valid uid')
