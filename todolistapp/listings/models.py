from django.db import models
from django.utils import timezone


# Create your models here.
	

class Listing(models.Model):
	tital = models.fields.CharField(max_length=100)
	

class Todolist(models.Model):
	item=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.item + self.details
		


		
