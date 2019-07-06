from blog.api import types
from blog.api import mutations
from blog.models import *

from graphene_django.filter import DjangoFilterConnectionField
import graphene


class Query(graphene.ObjectType):
	all_posts = graphene.List(types.PostType)

	folder = graphene.Field(types.FolderType, self_loc=graphene.Int())
	all_folders = DjangoFilterConnectionField(types.FolderType)

	category = graphene.relay.Node.Field(types.CategoryType)
	all_categories = DjangoFilterConnectionField(types.CategoryType)

	path = graphene.relay.Node.Field(types.PathType)
	all_paths = DjangoFilterConnectionField(types.PathType)

	all_mcqs = graphene.List(types.MCQType)

	mcq_tag = graphene.relay.Node.Field(types.MCQTagType)
	all_mcq_tags = DjangoFilterConnectionField(types.MCQTagType)


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

	def resolve_folder(self, info, **kwargs):
		self_loc = kwargs.get('self_loc')
		folder = Folder.objects.get(self_loc=self_loc)
		return folder



class Mutation:
	create_folder = mutations.CreateFolder.Field()
	update_folder = mutations.UpdateFolder.Field()
	create_post = mutations.CreatePost.Field()
	update_post = mutations.UpdatePost.Field()
	create_mcq = mutations.CreateMCQ.Field()
	update_mcq = mutations.UpdateMCQ.Field()
