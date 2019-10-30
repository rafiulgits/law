from django.db import models

class SupportBox(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	subject = models.CharField(max_length=50)
	message = models.TextField()
	date_time = models.DateTimeField(auto_now_add=True)
