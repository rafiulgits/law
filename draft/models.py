from django.db import models
from uuid import uuid4

class Article(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	title = models.CharField(max_length=250)
	body = models.TextField()
	label = models.CharField(max_length=50, default='')
	date_time = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)