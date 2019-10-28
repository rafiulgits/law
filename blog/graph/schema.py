from blog.graph import types
from blog.graph import mutations
from blog.models import *

from django.core.exceptions import ObjectDoesNotExist

from graphene_django.filter import DjangoFilterConnectionField
import graphene
from graphql_relay.node.node import from_global_id


class Query(graphene.ObjectType):
	post = graphene.Field(types.PostType, uid=graphene.ID())
	all_posts = graphene.List(types.PostType)

	folder = graphene.Field(types.FolderType, self_loc=graphene.String(), self_loc_uid=graphene.Int())
	all_folders = DjangoFilterConnectionField(types.FolderType)

	category = graphene.relay.Node.Field(types.CategoryType)
	all_categories = DjangoFilterConnectionField(types.CategoryType)

	path = graphene.relay.Node.Field(types.PathType)
	all_paths = DjangoFilterConnectionField(types.PathType)

	all_mcqs = DjangoFilterConnectionField(types.MCQType)

	mcq_tag = graphene.relay.Node.Field(types.MCQTagType)
	all_mcq_tags = DjangoFilterConnectionField(types.MCQTagType)

	all_mcq_labels = DjangoFilterConnectionField(types.MCQLabelType)

	all_cqs = graphene.List(types.CQType)

	all_mcq_issues = DjangoFilterConnectionField(types.MCQIssueType)
	mcq_issue = graphene.Field(types.MCQIssueType, uid=graphene.ID() )

	def resolve_post(self, info, **kwargs):
		uid = kwargs.get('uid')
		post = Post.objects.get(uid=uid)
		return post

	def resolve_all_posts(self, info, **kwargs):
		return Post.objects.all()

	def resolve_all_folders(self, info, **kwargs):
		self_loc_uid = kwargs.get('self_loc__uid', None)
		root_loc_uid = kwargs.get('root_loc__uid', None)
		if self_loc_uid:
			return Folder.objects.filter(self_loc_id=self_loc_uid)
		elif root_loc_uid:
			return Folder.objects.filter(root_loc_id=root_loc_uid)
		return Folder.objects.all()

	def resolve_all_categories(self, info, **kwargs):
		return Category.objects.all()

	def resolve_all_paths(self, info, **kwargs):
		return Path.objects.all()

	def resolve_all_mcqs(self, info, **kwargs):
		return MCQ.objects.all()

	def resolve_folder(self, info, **kwargs):
		self_loc_uid = kwargs.get('self_loc_uid', None)
		if self_loc_uid:
			try:
				return Folder.objects.get(self_loc=self_loc_uid)
			except ObjectDoesNotExist:
				return None
		self_loc = kwargs.get('self_loc', None)
		if self_loc:
			try:
				uid = from_global_id(self_loc)[1]
				return Folder.objects.get(self_loc=uid)
			except Exception:
				pass
		return None

	def resoleve_all_cqs(self, info, **kwargs):
		return CQ.objects.all()


	def resolve_mcq_issue(self, info, **kwargs):
		uid = kwargs.get('uid', None)
		if uid is None:
			raise ValueError("UID must be provided")
		try:
			obj = MCQIssue.objects.get(uid=uid)
			return obj
		except ObjectDoesNotExist:
			return None