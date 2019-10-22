from django.test import TestCase

from exam.models import *
from account.models import Account

class UserActivityTest(TestCase):
	def setUp(self):
		user = Account.objects.get(id=2)
		activity = UserActivity.objects.get(user=user)

	def test_activity_update(self):
		from json import loads
		exams = MCQExam.objects.filter(created_by = user)
		for exam in exams:
			stat = loads(exam.source.statistics)




