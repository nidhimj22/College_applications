from django.db import models

class application(models.Model):
	college_name =models.CharField(max_length=300) 
	department_name=models.CharField(max_length=300)
	deadline_date=models.DateTimeField('last date to apply')
	website=models.CharField(max_length=200)
	status=models.CharField(max_length=200) 
	comments=models.CharField(max_length=300)
	
	#  add/subtract  more as required  

	
# Create your models here.
