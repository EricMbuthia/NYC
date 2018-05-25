from django.db import models

# Create your models here.
class Users(models.Model):
	#filled by login with customer id going zero
	name=models.CharField(max_length=100)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length=100)
	customer_id = models.CharField(max_length=200,default="None")
	contact=models.CharField(max_length=20, default="None")
	authy_id=models.CharField(max_length=200)
	def __str__(self):
		return self.customer_id