from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=200, null=True)
	desc = models.CharField(max_length=2200, null=True)
	tag = models.CharField(max_length=200, null=True)
	dateCreate=models.DateField(max_length=350, null=True, blank=True)
	img=models.CharField(max_length=900, null=True, blank=True)
    
	def __str__(self):
		return self.title 