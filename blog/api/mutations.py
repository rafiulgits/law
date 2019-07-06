from blog.api import types
from blog.models import *
from django.core.exceptions import ObjectDoesNotExist
import graphene


class CreateCategory(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=True)

	category = graphene.Field(types.CategoryType)

	def mutate(self, info, name):
		category_obj = Category.objects.filter(name__iexact=name).first()
		if category_obj:
			return CreateCategory(category=None)
		category_obj = Category.objects.create(name=name)
		return CreateCategory(category=category_obj)


# class UpdateCategory(graphene.Mutation):
# 	class Arguments():
# 		uid = graphene.Int(required=True)
# 		name = graphene.String(required=True)

# 	category = graphene.Field(types.CategoryType)

# 	def mutate(self, info, uid, name):
# 		try:
# 			category_obj = Category.objects.get(uid=uid)
# 			category_obj.name = name
# 			category_obj.save()
# 			return UpdateCategory(category=category_obj)
# 		except ObjectDoesNotExist as e:
# 			return UpdateCategory(category=None)


class CreateFolder(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=True)
		distance = graphene.Int(required=True)
		category_uid = graphene.Int(required=True)
		root_loc_uid = graphene.Int(required=False)

	folder = graphene.Field(types.FolderType)

	def mutate(self,info,name,category_uid,distance,root_loc_uid=None):
		try:
			new_folder = Folder()
			category = Category.objects.get(uid=category_uid)
			if root_loc_uid:
				root_loc = Path.objects.get(uid=root_loc_uid)
				new_folder.root_loc = root_loc

			new_folder.self_loc = Path.objects.create()
			new_folder.name = name
			new_folder.category = category
			if root_loc_uid != None:
				new_folder.distance = distance
			new_folder.save()
			return CreateFolder(folder=new_folder)

		except ObjectDoesNotExist as e:
			return CreateFolder(folder=None)


class UpdateFolder(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=False)
		self_loc_uid = graphene.Int(required=True)
		root_loc_uid = graphene.Int(required=False)
		category_uid = graphene.Int(required=False)
		distance = graphene.Int(required=False)

	folder = graphene.Field(types.FolderType)

	def mutate(self, info,self_loc_uid,name=None,root_loc_uid=None,category_uid=None,distance=None):
		try:
			folder_obj = Folder.objects.get(self_loc_id=self_loc_uid)
			if name != None:
				folder_obj.name=name
			if category_uid != None:
				category = Category.objects.get(uid=category_uid)
				folder_obj.category = category
			if root_loc_uid != None:
				root_loc = Path.objects.get(uid=root_loc_uid)
				folder_obj.root_loc = root_loc
			if distance != None:
				folder_obj.distance = distance
			folder_obj.save()
			return UpdateFolder(folder=folder_obj)
		except ObjectDoesNotExist as e:
			return UpdateFolder(folder=None)


class CreatePost(graphene.Mutation):
	class Arguments():
		title = graphene.String(required=True)
		body = graphene.String(required=True)
		folder_loc = graphene.Int(required=True)

	post = graphene.Field(types.PostType)

	def mutate(self, info, title, body, folder_loc):
		try:
			folder = Folder.objects.get(self_loc_id=folder_loc)
			new_post = Post(title=title,body=body,folder=folder)
			new_post.save()
			return CreatePost(post=new_post)
		except ObjectDoesNotExist as e:
			return CreatePost(post=None)


class UpdatePost(graphene.Mutation):
	class Arguments():
		title = graphene.String(required=False)
		body = graphene.String(required=False)
		folder_loc = graphene.Int(required=False)
		uid = graphene.Int(required=True)

	post = graphene.Field(types.PostType)

	def mutate(self, info, uid, title=None, body=None, folder_loc=None):
		try:
			post_obj = Post.objects.get(uid=uid)
			if title is not None:
				post_obj.title = title
			if body is not None:
				post_obj.body = body
			if folder_loc is not None:
				folder = Folder.objects.get(self_loc_id=folder_loc)
				post_obj.folder = folder
			post_obj.save()
			return UpdatePost(post=post_obj)
		except ObjectDoesNotExist as e:
			return UpdatePost(post=post_obj)


class CreateMCQ(graphene.Mutation):
	class Arguments():
		question = graphene.String(required=True)
		option1 = graphene.String(required=True)
		option2 = graphene.String(required=True)
		option3 = graphene.String(required=True)
		option4 = graphene.String(required=True)
		answer = graphene.Int(required=True)
		summary = graphene.String(required=True)
		folder = graphene.Int(required=True)

	mcq = graphene.Field(types.MCQType)

	def mutate(self,info,question,option1,option2,option3,option4,answer,summary):
		new_mcq = MCQ()
		new_mcq.question=question
		new_mcq.option1=option1
		new_mcq.option2=option2
		new_mcq.option3=option3
		new_mcq.option4=option4
		new_mcq.answer=answer
		new_mcq.summary=summary
		new_mcq.save()
		return CreateMCQ(mcq=new_mcq)


class UpdateMCQ(graphene.Mutation):
	class Arguments():
		uid = graphene.Int(required=True)
		question = graphene.String(required=False)
		option1 = graphene.String(required=False)
		option2 = graphene.String(required=False)
		option3 = graphene.String(required=False)
		option4 = graphene.String(required=False)
		answer = graphene.Int(required=False)
		summary = graphene.String(required=False)

	mcq = graphene.Field(types.MCQType)

	def mutate(self,info,uid,question=None,option1=None,option2=None,option3=None,
		option4=None,answer=None,summary=None):

		try:
			mcq_obj = MCQ.objects.get(uid=uid)
			if question != None:
				mcq_obj.question=question
			if option1 != None:
				mcq_obj.option1=option1
			if option2 != None:
				mcq_obj.option2=option2
			if option3 != None:
				mcq_obj.option3=option3
			if option4 != None:
				mcq_obj.option4=option4
			if answer != None:
				mcq_obj.answer=answer
			if summary != None:
				mcq_obj.summary=summary
			mcq_obj.save()
			return UpdateMCQ(mcq=mcq_obj)
		except ObjectDoesNotExist as e:
			return UpdateMCQ(mcq=None)


class CreateCQ(graphene.Mutation):
	class Arguments():
		question = graphene.String(required=True)
	cq = graphene.Field(types.CQType)

	def mutate(self, info, question):
		cq_obj = CQ.objects.create(question=question)
		return CreateCQ(cq=cq_obj)


class UpdateCQ(graphene.Mutation):
	class Arguments():
		uid = graphene.Int(required=True)
		question = graphene.String(required=True)

	cq = graphene.Field(types.CQType)

	def mutate(self, info, uid, question):
		try:
			cq_obj = CQ.objects.get(uid=uid)
			cq_obj.question = question
			return UpdateCQ(cq=cq_obj)
		except ObjectDoesNotExist as e:
			return UpdateCQ(cq=cq_obj)


class CreateMCQTag(graphene.Mutation):
	class Arguments():
		mcq_uid = graphene.Int(required=True)
		folder_loc = graphene.Int(required=True)

	mcq_tag = graphene.Field(types.MCQTagType)

	def mutate(self, info, mcq_uid, folder_loc):
		try:
			mcq = MCQ.objects.get(uid=mcq_uid)
			folder = Folder.objects.get(self_loc_id=folder_loc)
			mcq_tag_obj = MCQTag.objects.create(mcq=mcq, folder=folder)
			return CreateMCQTag(mcq_tag=mcq_tag_obj)
		except ObjectDoesNotExist as e:
			return CreateMCQTag(mcq_tag=None)


class UpdateMCQTag(graphene.Mutation):
	class Arguments():
		uid = graphene.Int(required=True)
		mcq_uid = graphene.Int(required=True)
		folder_loc = graphene.Int(required=True)

	mcq_tag = graphene.Field(types.MCQTagType)

	def mutate(self, info, uid, mcq_uid, folder_loc):
		try:
			mcq_tag_obj = MCQTag.objects.get(uid=uid, mcq_uid=mcq_uid)
			folder = Folder.objects.get(self_loc_id=folder_loc)
			mcq_tag_obj.folder = folder
			mcq_tag_obj.save()
			return UpdateMCQTag(mcq_tag=mcq_tag_obj)
		except ObjectDoesNotExist as e:
			return UpdateMCQTag(mcq_tag=None)


class CreateCQTag(graphene.Mutation):
	class Arguments():
		cq_uid = graphene.Int(required=True)
		folder_loc = graphene.Int(required=True)

	cq_tag = graphene.Field(types.CQTagType)

	def mutate(self, info, cq_uid, folder_loc):
		try:
			cq = CQ.objects.get(uid=cq_uid)
			folder = Folder.objects.get(self_loc_id=folder_loc)
			cq_tag_obj = CQTag.objects.create(cq=cq, folder=folder)
			return CreateCQTag(cq_tag=cq_tag_obj)
		except ObjectDoesNotExist as e:
			return CreateCQTag(cq_tag=None)
		

class UpdateCQTag(graphene.Mutation):
	class Arguments():
		uid = graphene.Int(required=True)
		cq_uid = graphene.Int(required=True)
		folder_loc = graphene.Int(required=True)

	cq_tag = graphene.Field(types.CQTagType)

	def mutate(self, info, uid, cq_uid, folder_loc):
		try:
			cq_tag_obj = CQTag.objects.get(uid=uid, cq_uid=cq_uid)
			folder = Folder.objects.get(self_loc_id=folder_loc)
			cq_tag_obj.folder = folder
			cq_tag_obj.save()
			return UpdateCQTag(cq_tag=cq_tag_obj)
		except ObjectDoesNotExist as e:
			return CreateCQTag(cq_tag=None)