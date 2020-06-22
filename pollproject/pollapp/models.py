from django.db import models

# Create your models here.
class POLL(models.Model):
	question=models.CharField(max_length=100,null=True)

class Spoll(models.Model):
	data=[('Yes','yes'),('No','no')]
	opt=models.CharField(max_length=3,choices=data)

class Names(models.Model):
	name=models.CharField(max_length=30,null=True)
	def __str__(self):
		return self.name;