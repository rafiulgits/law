from exam.graph import types
from exam.graph import mutations
from exam.models import *

from graphene_django.filter import DjangoFilterConnectionField
import graphene


class Query(graphene.ObjectType):
	mcq_exam = graphene.Field(types.MCQExamType, uid=graphene.ID())
	all_mcq_exams = DjangoFilterConnectionField(types.MCQExamType)

	mcq_report = graphene.Field(types.MCQReportType, uid=graphene.ID())
	all_mcq_reports = DjangoFilterConnectionField(types.MCQReportType)

	mcq_exam_item = graphene.Field(types.MCQExamItemType, uid=graphene.ID())
	all_mcq_exam_items = DjangoFilterConnectionField(types.MCQExamItemType)

	clone_mcq_exam = graphene.Field(types.MCQExamCloneType, uid=graphene.ID())
	all_clone_mcq_exams = DjangoFilterConnectionField(types.MCQExamCloneType)

	omr = graphene.Field(types.OMRType, uid=graphene.ID())
	all_omrs = DjangoFilterConnectionField(types.OMRType)




class Mutation:
	create_mcq_exam = mutations.CreateMCQExam.Field()
	create_clone_mcq_exam = mutations.CreateCloneMCQExam.Field()
	create_mcq_exam_item = mutations.CreateMCQExamItem.Field()
	create_omr = mutations.CreateOMR.Field()