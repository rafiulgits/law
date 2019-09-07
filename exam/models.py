from account.models import Account
from blog.models import MCQ
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MCQReport(models.Model):
	uid = models.AutoField(primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	result = models.FloatField()
	date_time = models.DateTimeField(auto_now_add=True)


class MCQExam(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	level = models.SmallIntegerField(default=1)
	marks = models.PositiveIntegerField()
	total_mcq = models.PositiveIntegerField()
	public = models.BooleanField(default=False)
	created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	report = models.OneToOneField(MCQReport, on_delete=models.SET_NULL, null=True,blank=True)

	def __str__(self):
		return str(self.uid) + "-" + self.name


class MCQExamItem(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('mcq', 'exam')


class MCQExamClone(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	origin = models.ForeignKey(MCQExam, on_delete=models.SET_NULL, null=True)
	cloned_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	report = models.OneToOneField(MCQReport, on_delete=models.SET_NULL, null=True,blank=True)



class OMR(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	answer = models.SmallIntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
	correct = models.BooleanField()
	report = models.ForeignKey(MCQReport, on_delete=models.SET_NULL,null=True)
