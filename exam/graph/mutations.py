from django.core.exceptions import ObjectDoesNotExist

from exam.graph import types
from exam.models import *

import graphene


class CreateMCQExam(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=True)
		level = graphene.Int(required=True)
		total_mcq = graphene.Int(required=True)
		public = graphene.Boolean(required=True)
		created_by = graphene.ID(required=True)
		marks = graphene.Int(required=False)

	mcq_exam = graphene.Field(types.MCQExamType)

	def mutate(self, info,name,level,total_mcq,public,created_by,marks=None):
		new_mcq_exam = MCQExam(name=name,level=level,public=public,total_mcq=total_mcq)
		new_mcq_exam.created_by_id = created_by
		if marks:
			new_mcq_exam.marks = marks
		else:
			new_mcq_exam.marks = total_mcq

		report = MCQReport(user_id=created_by, result=0)
		report.save()
		new_mcq_exam.report = report
		new_mcq_exam.save()

		return CreateMCQExam(mcq_exam=new_mcq_exam)



class CreateCloneMCQExam(graphene.Mutation):
	class Arguments():
		name = graphene.String(required=True)
		origin_uid = graphene.ID(required=True)
		cloned_by = graphene.ID(required=True)


	clone_mcq_exam = graphene.Field(types.MCQExamCloneType)

	def mutate(self, info, name, origin_uid, cloned_by):
		new_clone_mcq_exam = MCQExamClone(name=name)
		new_clone_mcq_exam.origin_id = origin_uid
		new_clone_mcq_exam.cloned_by_id = cloned_by
		report = MCQReport(user_id=cloned_by, result=0)
		report.save()
		new_clone_mcq_exam.report = report
		new_clone_mcq_exam.save()

		return CreateCloneMCQExam(clone_mcq_exam=new_clone_mcq_exam)



class CreateMCQExamItem(graphene.Mutation):
	class Arguments():
		mcq_uid = graphene.ID(required=True)
		exam_uid = graphene.ID(required=True)

	mcq_exam_item = graphene.Field(types.MCQExamItemType)

	def mutate(self, info, mcq_uid, exam_uid):
		new_mcq_exam_item = MCQExamItem(mcq_id=mcq_uid,exam_id=exam_uid)
		new_mcq_exam_item.save()
		return CreateMCQExamItem(mcq_exam_item=new_mcq_exam_item)



class CreateOMR(graphene.Mutation):
	class Arguments():
		mcq_uid = graphene.ID(required=True)
		answer = graphene.Int(required=True)
		report_uid = graphene.ID(required=True)

	omr = graphene.Field(types.OMRType)

	def mutate(self, info, mcq_uid, answer, report_uid):
		try:
			mcq = MCQ.objects.get(uid=mcq_uid)
			new_omr = OMR(mcq_id=mcq_uid, report_id=report_uid, answer=answer)
			if mcq.answer == answer:
				new_omr.correct=True
			else:
				new_omr.correct=False
			new_omr.save()
			return CreateOMR(omr=new_omr)
		except ObjectDoesNotExist as e:
			return None