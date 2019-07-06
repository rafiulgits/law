from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from uuid import uuid4

_CATEGORIES = (
	('Subject', 'Subject'),
	('Part', 'Part'),
	('Chapter', 'Chapter'),
	('Topic', 'Topic'),
	('Module', 'Module'),
	('Label', 'Label')
)

_CATEGORIES_LIST = ['Subject', 'Part', 'Chapter', 'Topic', 'Module']

class Category(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=10, choices=_CATEGORIES, unique=True)

	def __str__(self):
		return self.name


class Path(models.Model):
	uid = models.AutoField(primary_key=True)

	def __str__(self):
		return str(self.uid)


class Folder(models.Model):
	name = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	self_loc = models.OneToOneField(Path,on_delete=models.CASCADE, primary_key=True,related_name='self_loc')
	root_loc = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='root_loc', null=True, blank=True)
	distance = models.SmallIntegerField(default=0)

	class Meta:
		unique_together = ('self_loc', 'root_loc')

	def __str__(self):
		return self.category.name +' - '+self.name


class Post(models.Model):
	uid = models.AutoField(primary_key=True)
	title = models.TextField(max_length=500)
	body = models.TextField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class MCQ(models.Model):
	uid = models.AutoField(primary_key=True)
	question = models.TextField()
	option1 = models.CharField(max_length=250)
	option2 = models.CharField(max_length=250)
	option3 = models.CharField(max_length=250)
	option4 = models.CharField(max_length=250)
	answer = models.SmallIntegerField(default=1,validators=[MaxValueValidator(4), MinValueValidator(1)])
	summary = models.CharField(max_length=250)

	def __str__(self):
		return self.question


class CQ(models.Model):
	uid = models.AutoField(primary_key=True)
	question = models.TextField()
	def __str__(self):
		return self.question


class MCQTag(models.Model):
	uid = models.BigAutoField(primary_key=True)
	mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE)
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('uid', 'folder')



class CQTag(models.Model):
	uid = models.AutoField(primary_key=True)
	cq = models.ForeignKey(CQ, on_delete=models.CASCADE)
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('cq', 'folder')