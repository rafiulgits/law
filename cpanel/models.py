from django.db import models

class SupportBox(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	subjet = models.CharField(max_length=50)
	message = models.TextField()
