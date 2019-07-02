from blog.models import Folder, MCQ, CQ, Post, Category, Path

from graphene import List, relay, ObjectType, Mutation
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class CategoryNode(DjangoObjectType):
	class Meta:
		model = Category
		filter_fields = {
			'uid' : ['exact'],
			'name' : ['exact', 'icontains']
		}
		interfaces = (relay.Node,)


class PathType(DjangoObjectType):
	class Meta:
		model = Path


class FolderNode(DjangoObjectType):
	class Meta:
		model = Folder
		filter_fields = {
			'name' : ['exact', 'icontains', 'istartswith'],
			'distance' : ['exact'],
			'category' : ['exact'],
			'category__name' : ['exact', 'icontains'],
			'category__uid' : ['exact'],
			'root' : ['exact'],
			'node' : ['exact']
		}
		interfaces = (relay.Node, )

class MCQType(DjangoObjectType):
	class Meta:
		model = MCQ


class CQType(DjangoObjectType):
	class Meta:
		model = CQ


class PostType(DjangoObjectType):
	class Meta:
		model = Post



class Query(ObjectType):
	all_posts = List(PostType)

	folder = relay.Node.Field(FolderNode)
	all_folders = DjangoFilterConnectionField(FolderNode)

	category = relay.Node.Field(CategoryNode)
	all_categories = DjangoFilterConnectionField(CategoryNode)

	all_paths = List(PostType)


	def resolve_all_posts(self, info, **kwargs):
		return Post.objects.all()

	def resolve_all_folders(self, info, **kwargs):
		return Folder.objects.all()

	def resolve_all_categories(self, info, **kwargs):
		return Category.objects.all()

	def resolve_all_paths(self, info, **kwargs):
		return Path.objects.all()



import graphene

class CreatePost(Mutation):
	class Arguments():
		title = graphene.String(required=True)
		body = graphene.String(required=True)
		folder = graphene.Int(required=True)

	post = graphene.Field(PostType)

	def mutate(self, info, title, body, folder):
		new_post = Post(title=title,body=body,folder_id=folder)
		new_post.save()
		return CreatePost(post=new_post)



class UpdatePost(Mutation):
	class Arguments():
		title = graphene.String(required=False)
		body = graphene.String(required=False)
		uid = graphene.Int(required=True)

	post = graphene.Field(PostType)

	def mutate(self, info, uid, title=None, body=None):
		post_obj = Post.objects.get(uid=uid)
		if title is not None:
			post_obj.title = title
		if body is not None:
			post_obj.body = body
		post_obj.save()
		return UpdatePost(post=post_obj)


class Mutation:
	create_post = CreatePost.Field()
	update_post = UpdatePost.Field()
