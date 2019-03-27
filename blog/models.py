from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

_CATEGORIES = (
	('Subject', 'Subject'),
	('Part', 'Part'),
	('Chapter', 'Chapter'),
	('Topic', 'Topic'),
	('Module', 'Module'),
	('Label', 'Label')
)


class Category(models.Model):
	name = models.CharField(max_length=10, primary_key=True, choices=_CATEGORIES)


class Path(models.Model):
	location = models.CharField(max_length=32, primary_key=True)



class Folder(models.Model):
	name = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	node = models.OneToOneField(Path, on_delete=models.CASCADE, primary_key=True,related_name='node')
	root = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='root')


class Post(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	title = models.TextField()
	body = models.TextField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)


class MCQ(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	question = models.TextField()
	option1 = models.TextField()
	option2 = models.TextField()
	option3 = models.TextField()
	option4 = models.TextField()
	answer = models.SmallIntegerField(default=1, 
		validators=[MaxValueValidator(4), MinValueValidator(1)])
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)


class CQ(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	question = models.TextField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)