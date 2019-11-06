from django.db import models
from uuid import uuid4



class Pointer(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)



class Directory(models.Model):
	name = models.CharField(max_length=250)
	self_loc = models.OneToOneField(Pointer,on_delete=models.CASCADE, 
			primary_key=True,related_name='self_loc')
	root_loc = models.ForeignKey(Pointer, on_delete=models.CASCADE, 
		related_name='root_loc', null=True, blank=True)
	class Meta:
		unique_together = ('self_loc', 'root_loc')

	def __str__(self):
		return self.name



class Article(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	title = models.CharField(max_length=250)
	body = models.TextField()
	directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
	label = models.CharField(max_length=50, default='')
	date_time = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title