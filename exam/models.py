from django.db import models

from account.models import Account
from blog.models import MCQ


class MCQReport(models.Model):
	uid = models.AutoField(primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	result = models.FloatField()
	date_time = models.DateTimeField(auto_now_add=True)


class MCQExam(models.Model):
	uid = models.AutoField(primary_key=True)
	level = models.SmallIntegerField(default=1)
	marks = models.PositiveIntegerField()
	total_mcq = models.PositiveIntegerField()
	public = models.BooleanField(default=False)
	created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	report = models.OneToOneField(MCQReport, on_delete=models.SET_NULL, null=True,blank=True)


class MCQExamItem(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('mcq', 'exam')


class MCQExamClone(models.Model):
	uid = models.AutoField(primary_key=True)
	origin = models.ForeignKey(MCQExam, on_delete=models.SET_NULL, null=True)
	cloned_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	report = models.OneToOneField(MCQReport, on_delete=models.SET_NULL, null=True,blank=True)



class OMR(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	correct = models.BooleanField()
	report = models.ForeignKey(MCQReport, on_delete=models.SET_NULL,null=True)
