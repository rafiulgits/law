from blog.api.types import *
from blog.models import *

import graphene


class CreatePost(graphene.Mutation):
	class Arguments():
		title = graphene.String(required=True)
		body = graphene.String(required=True)
		folder = graphene.Int(required=True)

	post = graphene.Field(PostType)

	def mutate(self, info, title, body, folder):
		new_post = Post(title=title,body=body,folder_id=folder)
		new_post.save()
		return CreatePost(post=new_post)



class UpdatePost(graphene.Mutation):
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

	mcq = graphene.Field(MCQType)

	def mutate(self,info,
			question,option1,option2,option3,option4,
			answer,summary,folder):
		folder = Folder.objects.get(node_id=folder)
		new_mcq = MCQ()
		new_mcq.question=question
		new_mcq.option1=option1
		new_mcq.option2=option2
		new_mcq.option3=option3
		new_mcq.option4=option4
		new_mcq.answer=answer
		new_mcq.summary=summary
		new_mcq.save()

		# tagging
		while folder != None:
			MCQTag.objects.create(mcq=new_mcq,tag=folder)
			if folder.distance != 0:
				folder = Folder.objects.get(node=folder.root)
			else:
				folder = None
				break
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

	mcq = graphene.Field(MCQType)

	def mutate(self,info,uid,
			question=None,option1=None,option2=None,option3=None,
			option4=None,answer=None,summary=None):
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
