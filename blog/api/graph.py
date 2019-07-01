from blog.models import Folder, MCQ, CQ, Post, Category, Path

import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class CategoryType(DjangoObjectType):
	class Meta:
		model = Category

class PathType(DjangoObjectType):
	class Meta:
		model = Path

class FolderType(DjangoObjectType):
	class Meta:
		model = Folder


class MCQType(DjangoObjectType):
	class Meta:
		model = MCQ


class CQType(DjangoObjectType):
	class Meta:
		model = CQ


class PostType(DjangoObjectType):
	class Meta:
		model = Post



class Query(object):
	all_posts = graphene.List(PostType)
	all_folders = graphene.List(FolderType)
	all_categories = graphene.List(CategoryType)
	all_paths = graphene.List(PathType)

	def resolve_all_posts(self, info, **kwargs):
		return Post.objects.all()

	def resolve_all_folders(self, info, **kwargs):
		return Folder.objects.all()

	def resolve_all_categories(self, info, **kwargs):
		return Category.objects.all()

	def resolve_all_paths(self, info, **kwargs):
		return Path.objects.all()