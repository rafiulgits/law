from django.db import models

from account.models import Account
from blog.models import MCQ


class MCQExam(models):
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	level = models.SmallIntegerField(default=1)
	marks = models.PositiveIntegerField()
	visible = models.BooleanField(default=False)
	created_by = models.ForeignKey(Account, on_delete=models.SET_NULL)
	date_time = models.DateTimeField(auto_now_add=True)


class MCQReport(models):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE)
	result = models.FloatField()
	date_time = models.DateTimeField(auto_now_add=True)


class OMR(models):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	correct = models.BooleanField()
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	report = models.ForeignKey(MCQReport, on_delete=models.SET_NULL)
