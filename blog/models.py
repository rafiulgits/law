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

_CATEGORIES_LIST = ['Subject', 'Part', 'Chapter', 'Topic', 'Module', 'Label']

class Category(models.Model):
	name = models.CharField(max_length=10, primary_key=True, choices=_CATEGORIES)

	def __str__(self):
		return self.name


class Path(models.Model):
	uid = models.UUIDField(editable=False, null=False, default=uuid4, primary_key=True)

	def __str__(self):
		return self.uid.hex



class Folder(models.Model):
	name = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	node = models.OneToOneField(Path, on_delete=models.CASCADE, primary_key=True,related_name='node')
	root = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='root', null=True, blank=True)
	url_path = models.TextField()
	distance = models.SmallIntegerField(default=0)

	def __str__(self):
		return self.category.name +' - '+self.name


class Post(models.Model):
	uid = models.UUIDField(editable=False, null=False, default=uuid4, primary_key=True)
	title = models.TextField()
	body = models.TextField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class MCQ(models.Model):
	uid = models.UUIDField(editable=False, null=False, default=uuid4, primary_key=True)
	question = models.TextField()
	option1 = models.TextField()
	option2 = models.TextField()
	option3 = models.TextField()
	option4 = models.TextField()
	answer = models.SmallIntegerField(default=1, 
		validators=[MaxValueValidator(4), MinValueValidator(1)])
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

	def __str__(self):
		return self.question


class CQ(models.Model):
	uid = models.UUIDField(editable=False, null=False, default=uuid4, primary_key=True)
	question = models.TextField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

	def __str__(self):
		return self.question