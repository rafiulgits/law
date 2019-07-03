from blog.api.types import *
from blog.api.mutations import *
from blog.models import *

from graphene_django.filter import DjangoFilterConnectionField
import graphene


class Query(graphene.ObjectType):
	all_posts = graphene.List(PostType)

	folder = graphene.Field(FolderType, node_uid=graphene.Int())
	all_folders = DjangoFilterConnectionField(FolderType)

	category = graphene.relay.Node.Field(CategoryType)
	all_categories = DjangoFilterConnectionField(CategoryType)

	path = graphene.Field(PathType, uid=graphene.Int())
	all_paths = graphene.List(PathType)

	all_mcqs = graphene.List(MCQType)

	mcq_tag = graphene.relay.Node.Field(MCQTagType)
	all_mcq_tags = DjangoFilterConnectionField(MCQTagType)


	def resolve_all_posts(self, info, **kwargs):
		return Post.objects.all()

	def resolve_all_folders(self, info, **kwargs):
		return Folder.objects.all()

	def resolve_all_categories(self, info, **kwargs):
		return Category.objects.all()

	def resolve_all_paths(self, info, **kwargs):
		return Path.objects.all()

	def resolve_all_mcqs(self, info, **kwargs):
		return MCQ.objects.all()

	def resolve_path(self, info, **kwargs):
		uid = kwargs.get('uid', None)
		return Path.objects.get(uid=uid)

	def resolve_folder(self, info, **kwargs):
		node_uid = kwargs.get('node_uid')
		folder = Folder.objects.get(node_id=node_uid)
		return folder



class Mutation:
	create_post = CreatePost.Field()
	update_post = UpdatePost.Field()
	# create_mcq = CreateMCQ.Field()
	# update_mcq = UpdateMCQ.Field()
