from blog.graph import types
from blog.models import *
from django.core.exceptions import ObjectDoesNotExist
import graphene


# Category
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


class DeleteCategory(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=True)

	category = graphene.Field(types.CategoryType)

	def mutate(self, info, name):
		category_obj = Category.objects.filter(name__iexact=name).first()
		if category_obj:
			category_obj.delete()
			return DeleteCategory(category=category_obj)
		return None



# MCQ
class CreateMCQ(graphene.Mutation):
	class Arguments():
		question = graphene.String(required=True)
		option1 = graphene.String(required=True)
		option2 = graphene.String(required=True)
		option3 = graphene.String(required=True)
		option4 = graphene.String(required=True)
		answer = graphene.Int(required=True)
		summary = graphene.String(required=True)
		level = graphene.Int(required=True)

	mcq = graphene.Field(types.MCQType)

	def mutate(self,info,question,option1,option2,option3,option4,answer,summary,level):
		new_mcq = MCQ()
		new_mcq.question=question
		new_mcq.option1=option1
		new_mcq.option2=option2
		new_mcq.option3=option3
		new_mcq.option4=option4
		new_mcq.answer=answer
		new_mcq.summary=summary
		new_mcq.level=level
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


class DeleteMCQ(graphene.Mutation):
	class Arguments():
		mcq_uid = graphene.ID(required=True)

	mcq = graphene.Field(types.MCQType)

	def mutate(self, info, mcq_uid):
		mcq_obj = MCQ.objects.filter(uid=mcq_uid).first()
		if mcq_obj:
			mcq_obj.delete()
			return DeleteMCQ(mcq=mcq_obj)
		return None


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


class DeleteMCQTag(graphene.Mutation):
	class Arguments():
		mcq_tag_uid = graphene.ID(required=True)

	mcq_tag = graphene.Field(types.MCQTagType)

	def mutate(self, info, mcq_tag_uid):
		mcq_tag_obj = MCQTag.objects.filter(uid=mcq_tag_uid).first()
		if mcq_tag_obj:
			mcq_tag_obj.delete()
			return DeleteMCQTag(mcq_tag=mcq_tag_obj)
		return None


# CQ
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


class DeleteCQ(graphene.Mutation):
	class Atguments():
		cq_uid = graphene.ID(required=True)

	cq = graphene.Field(types.CQType)

	def mutate(self, info, cq_uid):
		cq_obj = CQ.objects.filter(uid=cq_uid).first()
		if cq_obj:
			cq_obj.delete()
			return DeleteCQ(cq=cq_obj)
		return None


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


class DeleteCQTag(graphene.Mutation):
	class Arguments():
		cq_tag_uid = graphene.ID(required=True)

	cq_tag = graphene.Field(types.CQTagType)

	def mutate(self, info, cq_tag_uid):
		cq_tag_obj = CQTag.objects.filter(uid=cq_tag_uid).first()
		if cq_tag_obj:
			cq_tag_obj.delete()
			return DeleteCQTag(cq_tag=cq_tag_obj)
		return None
