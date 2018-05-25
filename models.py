from django.db import models
from authetr.models import Users
# Create your models here.

class UserInfo(models.Model):#compare alphabets of cus_id and card_id and initiate search
	#name filled from the login after table has been formed
	#first card, email or bank id will be stored through here
	customer_id=models.ForeignKey("authetr.Users", on_delete=models.CASCADE)
	name= models.CharField(max_length=100, default="None")
	contact=models.CharField(max_length=100,default="None")
	no_tickets=models.CharField(max_length=3, default="None")#value will always change
	balance_id=models.CharField(max_length=200,default="None")#value will always change
	card_present=models.CharField(max_length=200, default="None")#user has card_id or not
	pay_pal_present=models.CharField(max_length=200, default="None")#user has paypal_id account or not
	bank_id_present=models.CharField(max_length=200, default="None")#user has bank account or not
	def __str__(self):
		return self.name
class FacebookInfo(models.Model): #anyone who uses this to log in they will get an fb mail and a inserted in User
	fb_username=models.CharField(max_length=50)
	fb_mail=models.CharField(max_length=200)
	fb_id=models.CharField(max_length=200)
	customer_id=models.CharField(max_length=200)
	password = models.CharField(max_length=100)
	def __str__(self):
		return self.fb_username
class TwitterInfo(models.Model): #anyone who uses this to log in they will get an fb mail and a inserted in User
	tw_username=models.CharField(max_length=50)
	tw_mail=models.CharField(max_length=200)
	tw_id=models.CharField(max_length=200)
	customer_id=models.CharField(max_length=200)
	password = models.CharField(max_length=100)
	def __str__(self):
		return self.tw_username
class GoogleInfo(models.Model): #anyone who uses this to log in they will get an fb mail and a inserted in User
	gg_username=models.CharField(max_length=50)
	gg_mail=models.CharField(max_length=200)
	gg_id=models.CharField(max_length=200)
	customer_id=models.CharField(max_length=200)
	password = models.CharField(max_length=100)
	def __str__(self):
		return self.gg_username
#class MyCards(models.Model):
	#from the card form
	#customer_id = models.ForeignKey("authetr.Users",on_delete=models.CASCADE, related_name='cus_id')
	#cvv = models.CharField(max_length=4)
	#card_number = models.CharField(max_length=18,default="None")

	#expiry_month=models.CharField(max_length=2,default="00")
	#expiry_year=models.CharField(max_length=4,default="0000")
	#expiry_date = models.DateTimeField(blank=True,null=True)
	#card_id = models.CharField(max_length = 200,default="None")
	#holder_name= models.ForeignKey(UserInfo,on_delete=models.CASCADE)
	#balance_id=models.CharField(max_length=200, default="None")#last id
	#email=models.ForeignKey(Users, on_delete=models.CASCADE,related_name='mail')
	#def __str__(self):
		#return self.card_id
class Cards(models.Model):
	#from the card form
	customer_id = models.ForeignKey("authetr.Users",on_delete=models.CASCADE, related_name='cus_id2')
	#cvv = models.CharField(max_length=4)
	card_number = models.CharField(max_length=18,default="None")
	expiry_month=models.CharField(max_length=2,default="00")
	expiry_year=models.CharField(max_length=4,default="0000")
	#expiry_date = models.DateTimeField(blank=True,null=True)
	card_id = models.CharField(max_length = 200,default="None")
	#holder_name= models.ForeignKey(UserInfo,on_delete=models.CASCADE)
	#balance_id=models.CharField(max_length=200, default="None")#last id
	#email=models.ForeignKey(Users, on_delete=models.CASCADE,related_name='mail')
	def __str__(self):
		return self.card_id
class PayPal(models.Model):
	customer_id=models.ForeignKey("authetr.Users", on_delete=models.CASCADE)
	email=models.CharField(max_length=200)
	paypal_id=models.CharField(max_length=200)
	balance_id=models.CharField(max_length=200)
	def __str__(self):
		return self.email
class Banks(models.Model):
	customer_id=models.ForeignKey("authetr.Users", on_delete=models.CASCADE)
	bank_id=models.CharField(max_length=200)
	bank_name=models.CharField(max_length=100)
	name=models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	account_number=models.CharField(max_length=200)
	city=models.CharField(max_length=50)
	balance_id=models.CharField(max_length=200)
	def __str__(self):
		return self.name
class TicketsStore(models.Model):
	#buy tickets by Admin
	ticket_type=models.CharField(max_length=15)
	cost=models.CharField(max_length=10)
	unitDistance=models.CharField(max_length=10)
	durationTime=models.TimeField()
	creation_date_time=models.DateTimeField()
	update_date_time=models.DateTimeField()
	expiry_date_time=models.DateTimeField()
	def __str__(self):
		return self.ticket_type
class Tickets(models.Model):
	#buy Tickets
	customer_id=models.ForeignKey("authetr.Users", on_delete=models.CASCADE)
	ticket_stamp_id=models.CharField(max_length=200)#auto generated fingerprint from charge
	ticket_type=models.ForeignKey(TicketsStore, on_delete=models.CASCADE)
	number_of_tickets=models.CharField(max_length=200,default=0)
	cash_paid=models.CharField(max_length=10,default="None")
	number_of_children=models.CharField(max_length=10, default=0)
	number_of_adults=models.CharField(max_length=10, default=0)
	nyc_id=models.CharField(max_length=200,default="None")
	charge_id=models.CharField(max_length=200, default="None")
	distance=models.CharField(max_length=10,default="None")
	time_bought=models.DateTimeField()
	expiry_date_time=models.DateTimeField()
	tickets_used=models.CharField(max_length=15,default="None")
	issued_to=models.CharField(max_length=200,default="Nobody")
	def __str__(self):
		return self.issued_to

#Logs for the passenger
class RegFinance(models.Model):
	payment_method=models.CharField(max_length=60)
	payment_method_id=models.CharField(max_length=200)
	time_of_reg=models.DateTimeField()
	time_of_rec=models.DateTimeField()
	location_lat=models.CharField(max_length=50)
	location_lon=models.CharField(max_length=50)
	device_type=models.CharField(max_length=200)
	def __str__(self):
		return self.time_of_reg
class FinanceTransac(models.Model):
	customer_id=models.ForeignKey("authetr.Users", on_delete=models.CASCADE)
	recepient_id=models.CharField(max_length=200)
	transaction_id=models.CharField(max_length=200)
	date_record_creation=models.DateTimeField()
	date_of_transaction=models.DateTimeField()
	amount_of_cash=models.CharField(max_length=10)
	location_lat=models.CharField(max_length=50)
	location_lon=models.CharField(max_length=50)
	device_type=models.CharField(max_length=200)
	def __str__(self):
		return self.date_of_transaction
class DailyActivities(models.Model):
	activity=models.TextField(max_length=2000)
	time_of_activity=models.DateTimeField()
	time_of_rec=models.DateTimeField()
	location_lat=models.CharField(max_length=50)
	location_lon=models.CharField(max_length=50)
	device_type=models.CharField(max_length=200)
	def __str__(self):
		return self.activity
class BusFare(models.Model):
	destination=models.CharField(max_length=200)
	fare=models.CharField(max_length=200) 
	def __str__(self):
		return self.destination


