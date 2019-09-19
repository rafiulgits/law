from account.models import Account
from blog.models import MCQ
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class MCQExamSource(models.Model):
	uid = models.AutoField(primary_key=True)
	public = models.BooleanField(default=False)
	created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	total_mcq = models.PositiveSmallIntegerField()
	duration = models.PositiveSmallIntegerField()
	statistics = models.TextField()
	
	def __str__(self):
		return str(self.uid)


class MCQExamItem(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	exam = models.ForeignKey(MCQExamSource, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('mcq', 'exam')



class MCQExam(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	is_clone = models.BooleanField(default=False)
	is_public = models.BooleanField(default=False)
	source = models.ForeignKey(MCQExamSource, on_delete=models.CASCADE)
	created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.uid) + "-" + self.name



class MCQReport(models.Model):
	uid = models.AutoField(primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	exam = models.OneToOneField(MCQExam, on_delete=models.CASCADE)
	total_correct = models.PositiveSmallIntegerField()
	total_wrong = models.PositiveSmallIntegerField()
	total_blank = models.PositiveSmallIntegerField()
	result = models.FloatField()
	date_time = models.DateTimeField(auto_now_add=True)



class OMR(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	answer = models.SmallIntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
	correct = models.BooleanField()
	report = models.ForeignKey(MCQReport, on_delete=models.SET_NULL,null=True)
