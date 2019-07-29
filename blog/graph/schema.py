from blog.graph import types
from blog.graph import mutations
from blog.models import *

from graphene_django.filter import DjangoFilterConnectionField
import graphene


class Query(graphene.ObjectType):
	post = graphene.Field(types.PostType, uid=graphene.ID())
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

	all_cqs = graphene.List(types.CQType)

	def resolve_post(self, info, **kwargs):
		uid = kwargs.get('uid')
		post = Post.objects.get(uid=uid)
		return post

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

	def resoleve_all_cqs(self, info, **kwargs):
		return CQ.objects.all()



class Mutation:
	create_category = mutations.CreateCategory.Field()
	# update_category = mutations.UpdateCategory.Field()

	create_folder = mutations.CreateFolder.Field()
	update_folder = mutations.UpdateFolder.Field()
	
	create_post = mutations.CreatePost.Field()
	update_post = mutations.UpdatePost.Field()
	
	create_mcq = mutations.CreateMCQ.Field()
	update_mcq = mutations.UpdateMCQ.Field()

	create_cq = mutations.CreateCQ.Field()
	update_cq = mutations.UpdateCQ.Field()

	create_mcq_tag = mutations.CreateMCQTag.Field()
	update_mcq_tag = mutations.UpdateMCQTag.Field()

	create_cq_tag = mutations.CreateCQTag.Field()
	update_cq_tag = mutations.UpdateCQTag.Field()