from django.core.exceptions import ObjectDoesNotExist


from exam.graph import types
from exam.models import *

from graphene_django.filter import DjangoFilterConnectionField
import graphene


class Query(graphene.ObjectType):
	mcq_exam = graphene.Field(types.MCQExamType, uid=graphene.ID())
	all_mcq_exams = DjangoFilterConnectionField(types.MCQExamType)

	mcq_report = graphene.Field(types.MCQReportType, uid=graphene.ID())
	all_mcq_reports = DjangoFilterConnectionField(types.MCQReportType)

	all_mcq_exam_items = DjangoFilterConnectionField(types.MCQExamItemType)

	all_omrs = DjangoFilterConnectionField(types.OMRType)


	def resolve_mcq_exam(self, info, **kwargs):
		uid = kwargs.get('uid', None)
		if uid is None:
			raise ValueError('you must provide uid')
		try:
			obj = MCQExam.objects.get(uid=uid)
			return obj
		except ObjectDoesNotExist:
			raise ValueError('must provide an valid uid')


	def resolve_all_mcq_exams(self, info, **kwargs):
		created_by = kwargs.get('created_by', None)
		if created_by is not None:
			return MCQExam.objects.filter(created_by_id=created_by)
		return MCQExam.objects.all()



	def resolve_all_omrs(self, info, **kwargs):
		report_uid = kwargs.get('report_uid', None)
		if report_uid:
			return OMR.objects.filter(report_id=report_uid)
		return None