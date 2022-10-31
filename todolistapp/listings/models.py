from django.db import models
from django.utils import timezone


# Create your models here.

	
	#this creates clas, band, inherits from modelsModel (djangos model base class)
	#add class attribute to the name. assigns CharField (which is short for character field)
	#this field will sotre characer/text/string data
	#max lengt set to 100
	#django framework creates constructor for you don't need to do __init__ like python class
	

class Listing(models.Model):
	tital = models.fields.CharField(max_length=100)
	

class Todolist(models.Model):
	item=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.item + self.details
		


		