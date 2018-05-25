from django.shortcuts import render,redirect
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponseRedirect

from django.utils import timezone
from django.views.generic import *
from authetr.models import Users

from .forms import*
from .models import*
import random
from random import SystemRandom

import datetime
import stripe
SEC_KEY = settings.SECRET_STRIPE_KEY
PUB_KEY = 'PUBLIC_STRIPE_KEY'
stripe.api_key=SEC_KEY
cus_id=""
url_dict=dict()
past_url=""
sysrand = SystemRandom()

# Create your views here.
def home(request):
	cus_id=request.session["username"]
	return render(request,"passenger/home.html")
class CardList(ListView):
	if cus_id == "":
		cus_id="cus_CuqmwOld6Yvc8L"#request.session["username"]
	else:
		print("cus_id is" +cus_id)
	#model = Cards
	#template_name = 'passenger/paymentMethod.html'

	#def get_queryset(self):
		#cus_id=self.request.session["username"]
		#min_amount = self.request.GET.get('min_amount')
        #max_amount = self.request.GET.get('max_amount')
		#return Adverts.objects.filter(amount__range=(min_amount, max_amount))
		#return Cards.objects.filter(customer_id=cus_id)
	customer_id_reference=Users.objects.get(customer_id=cus_id)
	#cus_id_reference=Users.objects.get(customer_id=cus_id)
	queryset = Cards.objects.filter(customer_id=customer_id_reference)
	template_name = 'passenger/paymentMethodUse.html'
class CardListForManager(ListView):
	if cus_id == "":
		cus_id="cus_CuqmwOld6Yvc8L"#request.session["username"]
	else:
		print("cus_id is" +cus_id)
	#model = Cards
	#template_name = 'passenger/paymentMethod.html'

	#def get_queryset(self):
		#cus_id=self.request.session["username"]
		#min_amount = self.request.GET.get('min_amount')
        #max_amount = self.request.GET.get('max_amount')
		#return Adverts.objects.filter(amount__range=(min_amount, max_amount))
		#return Cards.objects.filter(customer_id=cus_id)
	customer_id_reference=Users.objects.get(customer_id=cus_id)
	#cus_id_reference=Users.objects.get(customer_id=cus_id)
	queryset = Cards.objects.filter(customer_id=customer_id_reference)
	template_name = 'passenger/paymentMethodManager.html'
class CardDetailForManagement(DetailView):
	model=Cards
	template_name = 'passenger/paymentMethodDetailManagement.html'
class CardDetail(DetailView):
	model=Cards
	template_name = 'passenger/paymentMethodDetail.html'
class TicketList(ListView):
	if cus_id == "":
		cus_id="cus_CuqmwOld6Yvc8L"#request.session["username"]
	#model = Cards
	#template_name = 'passenger/paymentMethod.html'

	#def get_queryset(self):
		#cus_id=self.request.session["username"]
		#min_amount = self.request.GET.get('min_amount')
        #max_amount = self.request.GET.get('max_amount')
		#return Adverts.objects.filter(amount__range=(min_amount, max_amount))
		#return Cards.objects.filter(customer_id=cus_id)
	customer_id_reference=Users.objects.get(customer_id=cus_id)
	#cus_id_reference=Users.objects.get(customer_id=cus_id)
	queryset = Tickets.objects.filter(customer_id=customer_id_reference)
	template_name = 'passenger/ticketList.html'
class TicketDetail(DetailView):
	model=Tickets
	template_name = 'passenger/ticketDetail.html'
def paymentMethod23(request):
	print("Back to sender")
	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	#return #HttpRequest.request.META['HTTP_REFERER']#.get('HTTP_REFERER')
	#retrieve card from online
	#show its details 
def viewTickets(request):
	#customer_id
	pass
def useTicket(request,id):
	request.session['tickettt_id']=id
	form=PayById()
	return render(request, "passenger/payCabTicket.html",{'form':form});
def payTicket(request):
	if request.method == "POST" and request.is_ajax:
		id=	request.session['tickettt_id']
		form=PayById(data=request.POST)
		driver_id= request.POST["driver_id"];
		issue=Tickets.objects.get(id=id)
		issue.issued_to=driver_id
		issue.save()		
		#Update in db
		return render(request, "passenger/payCabTicket.html",{'form':form});
def choosePaymentMethod(request):
	cus_id=request.session["username"]
	if request.method== "GET":
		return render (request,'passenger/paymentMethod.html',{'form':form})
	#add card online and in local db
	elif request.method=="POST" and request.is_ajax:
		form= BuyMultiplePasses(data=request.POST)
		if form.is_valid():
			children_number = request.POST["children_number"];
			adult_number = request.POST["adult_number"];
			passenger_id = request.POST["passenger_id"];
			print("children_number")
			print(children_number)
			print("adult_number")
			print(adult_number)
			print("passenger_id")
			print(passenger_id)
			
			response_data = {'received': True, 'errors':  str(form.errors),'status':'ok',}
			return JsonResponse(response_data)
		else:
			print("formerrors")
			print(form.errors)
			response_data = {'received': False, 'errors':  str(form.errors),'status':'not_ok'}
			return JsonResponse(response_data)
	else:
		form=AddPaypal()
		print("app has gone crazy")
		return render(request,'passenger/chooseTicket.html')		
	pass	
def error(request):
	return render(request,"passenger/error.html")
def create_customer(request,token="", description="",email=""):
	#get customer id from api
	customer=stripe.Customer.create(source=token, description=description,email=email)
	#get data from update card
	#update User model in authetr
	pass
def update_customer(request,token, cus_id,details_dict):
	#start with online and then locally
	#update online and locally
	#populate form with details ever
	cu = stripe.Customer.retrieve(cus_id)
	cu.description=details_dict["description"]
	cu.name=details_dict["name"]
	cu.email=details_dict["email"]
	cu.save()
	pass
def deleteCustomer(request,token, cus_id):
	#delete online and locally
	pass
def retrieve_customer(request,token, cus_id):
	customer=stripe.Customer.retrieve(cus_id)
	#start with online then locally
	#retrieve online and locally
	return customer
def addCard(request):
	cus_id=request.session["username"]
	customer_id=request.user.username
	print("customer_id")
	print(customer_id)
	if request.method== "GET":
		#form=AddCard()
		#past_url=""
		current_url="http://"+request.META.get('HTTP_HOST','/')+"/passenger/addCard/"
		if request.META.get('HTTP_REFERER','//') != current_url:
			request.session["past_url"]=request.META.get('HTTP_REFERER','//')
			return render(request,'passenger/addCard.html')
		else:
		#print("meta REFERER first")
		#print(request.META.get('HTTP_REFERER','//'))
		#print("meta HOST first")
		#print(request.META.get('HTTP_HOST','/'))
		#print("current_url")
		#print(current_url)
			return render(request,'passenger/addCard.html')
	#add card online and in local db
	else:
		token = request.POST.get('stripeToken')
		print("token Card")
		print(token)
		print("Customer")
		card_id=""
		save_card=Cards()
		customer_id_reference=Users.objects.get(customer_id=customer_id)
		customer = stripe.Customer.retrieve(customer_id )
		print(customer)
		card=customer.sources.create(source=token)
		card_id=card.id
		card_number=card.last4
		expiry_month=card.exp_month
		expiry_year=card.exp_year
		save_card=Cards(customer_id=customer_id_reference,
			card_id=card_id,card_number=card_number,expiry_month=expiry_month,expiry_year=expiry_year)		
		save_card.save()
		print("card just saved")
		#request.session["first"]="Send_Me_Back"
		past_u=request.session["past_url"]
		return HttpResponseRedirect(request.session["past_url"])

		#return HttpRequest.META.get('HTTP_REFERER')#render(request,'passenger/addCard.html')
	#store card locally	
	#populate addcard



def retrieveCard(request,customer_id, cardNumber):
	customer = stripe.Customer.retrieve(customer_id)
	#card id form the db
	card_id=""
	card = customer.sources.retrieve(card_id)
	# if card exists call the create charge
	pass
def updateCard(request,customer_id,card_id,details_dict):
	#update online then locally
	customer = stripe.Customer.retrieve(customer_id)
	card = customer.sources.retrieve(card_id)
	card.name = details_dict["name"]
	#and many more
	card.save()
	pass
def deleteCard(request,customer_id,card_id):
	customer = stripe.Customer.retrieve(customer_id)
	customer.sources.retrieve(card_id).delete()
	pass


def listCards(request,customer_id):
	card_list=stripe.Customer.retrieve(customer_id).sources.all(object='card')
	pass
def calcTicketStamp():
	print("system random")
	print(random.randrange(0,9))
	#sysrand.randbelow(10)
	count=1
	addition= 1
	stamp=0
	return str(stamp)
# See shared sources card
def createCharge(request,card_email_id,payment_method):
	#transfer cash from one user to another.
	#ask confirmation if they want to pay to a certain driver 

	#transfer cash from account to user
	#store charge details incase of too much requests
	# view Create a payout

	customer_id=request.session["username"]
	customer_id_reference= Users.objects.get(customer_id=customer_id)
	amount=request.session["amount_cost"]
	invoice=request.session["invoice"]
	children_pass_num=invoice["children_pass_num"]
	adult_pass_num=invoice["adult_pass_num"]
	passenger_id=invoice["passenger_id"]
	tickets_dict=request.session["tickets_dict"]
	tickets_list=request.session["tickets_list"]
	total_passengers=invoice["total_passengers"]
	customer = stripe.Customer.retrieve(customer_id)
	#card id or email form the db
	
	try:

		if payment_method=="card":
			print(tickets_list)
			card_id=Cards.objects.get(id=card_email_id).card_id
			print(card_id)	
			print("card doing")
			charge=stripe.Charge.create(
  amount=2000,
  currency="usd",
  customer=customer_id,
  source=card_id, 
  description="Charge for name",)
			print("chargeID")
			print(charge.id)
			if passenger_id != None:
				print("start of first for:--> "+str(timezone.now()))
				current_tz = timezone.get_current_timezone()
				for  t  in tickets_dict:
					tickets_store_reference= TicketsStore.objects.get(ticket_type=t)
					ticket_record=Tickets(customer_id=customer_id_reference,ticket_stamp_id=calcTicketStamp(),ticket_type=tickets_store_reference
					,number_of_tickets="1",number_of_children="0",number_of_adults=1,nyc_id=passenger_id,
					charge_id=charge.id,distance="2",time_bought=timezone.now(),expiry_date_time="2011-09-01T13:20:30+03:00"
,tickets_used="0")
					ticket_record.save()
				print("start of second for:--> "+str(datetime.datetime.now()))
				for to in tickets_list:
					count=1
					tickets_store_reference2= TicketsStore.objects.get(ticket_type=to["Type"])
					ticket_record2=Tickets(customer_id=customer_id_reference,ticket_stamp_id=calcTicketStamp(),ticket_type=tickets_store_reference2
					,number_of_tickets=str(int(to["Type_adult"])+int(to["Type_children"])),number_of_children=to["Type_children"],number_of_adults=to["Type_adult"],
					charge_id=charge.id,distance="2",time_bought=timezone.now(),expiry_date_time="2011-09-01T13:20:30+03:00"
,tickets_used="0")
					ticket_record2.save()
					count=count+1
				print("done with first and second for--> "+str(datetime.datetime.now()))
		elif payment_method == "email":
			pass
		elif payment_method == "bank":
			pass
			#store details in db even chargeId
	#except stripe.error.CardError as e:
		#raise "Your card is not valid"
	except Exception as e:
		raise "There was a problem with the transaction  "+str(e)
	return render(request, 'passenger/buyMultipleTickets.html') 
def buyTickets(request):
	calcTicketStamp()
	cus_id=request.session["username"]
	if request.method== "GET":
		form=BuyMultiplePasses()
		return render (request,'passenger/buyMultipleTickets.html',{'form':form})
	#add card online and in local db
	elif request.method=="POST" and request.is_ajax:
		form= BuyMultiplePasses(data=request.POST)
		customer_id_reference= Users.objects.get(customer_id=cus_id)
		
		tickets_dict_other=dict() 
		tickets_list=list()
		invoice=dict()
		total_passengers=0
		children_pass_num=0
		adult_pass_num=0

		destination="Nyahururu"
		if form.is_valid():
			type_1_children_number = request.POST.get("type_1_children_number",False);
			type_1_adult_number = request.POST.get("type_1_adult_number", False)
			type_2_children_number = request.POST.get("type_2_children_number",False);
			type_2_adult_number = request.POST.get("type_2_adult_number", False)
			type_3_children_number = request.POST.get("type_3_children_number");
			type_3_adult_number = request.POST.get("type_3_adult_number", False)
			type_4_children_number = request.POST.get("type_4_children_number")
			type_4_adult_number = request.POST.get("type_4_adult_number", False)		
			type_5_children_number = request.POST.get("type_5_children_number",False)
			type_5_adult_number = request.POST.get("type_5_adult_number", False)		
			passenger_id = request.POST.get("passenger_id",False);
			type_1_ticket = request.POST.get("type_1_ticket",False);
			type_2_ticket = request.POST.get("type_2_ticket",False);
			type_3_ticket = request.POST.get("type_3_ticket",False);
			type_4_ticket = request.POST.get("type_4_ticket",False);
			type_5_ticket = request.POST.get("type_5_ticket",False);
			if type_1_children_number.isdigit():#!= None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type1"
				tickets_dict_other["Type_children"]=type_1_children_number
				total_passengers = total_passengers+int(type_1_children_number)
				children_pass_num=children_pass_num+int(type_1_children_number)
			if type_1_adult_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type1"
				tickets_dict_other["Type_adult"]=type_1_adult_number
				total_passengers = total_passengers+int(type_1_adult_number)
				adult_pass_num=adult_pass_num+int(type_1_adult_number)
			tickets_list.append(tickets_dict_other)
			if type_2_children_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type2"
				tickets_dict_other["Type_children"]=type_2_children_number
				print("type_2_children_number")
				print(type_2_children_number)
				total_passengers = total_passengers+int(type_2_children_number)
				children_pass_num=children_pass_num+int(type_2_children_number)
			if type_2_adult_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type2"
				tickets_dict_other["Type_adult"]=type_2_adult_number
				total_passengers = total_passengers+int(type_2_adult_number)
				adult_pass_num=adult_pass_num+int(type_2_adult_number)
			tickets_list.append(tickets_dict_other)
			if type_3_children_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type3"
				tickets_dict_other["Type_children"]=type_3_children_number
				total_passengers = total_passengers+int(type_3_children_number)
				children_pass_num=children_pass_num+int(type_3_children_number)
			if type_3_adult_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type3"
				tickets_dict_other["Type_adult"]=type_3_adult_number
				total_passengers = total_passengers+int(type_3_adult_number)
				adult_pass_num=adult_pass_num+int(type_3_adult_number)
			tickets_list.append(tickets_dict_other)
			if type_4_children_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type4"
				tickets_dict_other["Type_children"]=type_4_children_number
				total_passengers = total_passengers+int(type_4_children_number)
				children_pass_num=children_pass_num+int(type_4_children_number)
			if type_4_adult_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type4"
				tickets_dict_other["Type_adult"]=type_4_adult_number
				total_passengers = total_passengers+int(type_4_adult_number)
				adult_pass_num=adult_pass_num+int(type_4_adult_number)
			tickets_list.append(tickets_dict_other)
			if type_5_children_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type5"
				tickets_dict_other["Type_children"]=type_5_children_number
				total_passengers = total_passengers+int(type_5_children_number)
				children_pass_num=children_pass_num+int(type_5_children_number)
			if type_5_adult_number.isdigit():# != None:
				tickets_dict=dict() 
				tickets_dict_other["Type"]="Type5"
				tickets_dict_other["Type_adult"]=type_5_adult_number
				total_passengers = total_passengers+int(type_5_adult_number)
				adult_pass_num=adult_pass_num+int(type_5_adult_number)
			tickets_list.append(tickets_dict_other)
			request.session["tickets_list"]=tickets_list
		
#search for the empty and full ones.
			if type_1_ticket == "Type1":
				tickets_dict["Type1"]="Type1"
				print("type 1 is "+type_1_ticket)
			if type_2_ticket == "Type2":	
				tickets_dict["Type2"]="Type2"
			if type_3_ticket == "Type3":
				tickets_dict["Type3"]="Type3"
			if type_4_ticket == "Type4":
				tickets_dict["Type4"]="Type4"
			if type_5_ticket == "Type5":
				tickets_dict["Type5"]="Type5"
			if passenger_id != None:
				total_passengers = total_passengers +1
				invoice["passenger_id"]=passenger_id
				#now = datetime.datetime.now()
	
			
			#destination from db
			destination="Rumuruti"
			amount_cost=calculate_cost(tickets_dict,destination)
			request.session["amount_cost"]=amount_cost
			invoice["amount_cost"]=amount_cost
			invoice["total_passengers"]=total_passengers
			invoice["children_pass_num"]=children_pass_num
			invoice["adult_pass_num"]=adult_pass_num


			request.session["tickets_dict"]=tickets_dict
			customer_id=request.session["username"]#from session
			#createCharge(amount,card_id,payment_method)
			request.session["invoice"]=invoice
			#payment_url="http://"+request.META.get('HTTP_HOST','/')+"/passenger/paymentMethod"
			#return render(request,"passenger/paymentMethodUse.html")
			#return redirect(payment_url)
			response_data = {'received': True, 'errors':  str(form.errors),'status':'ok'}
			return JsonResponse(response_data)
		else:
			print("formerrors")
			print(form.errors)
			response_data = {'received': False, 'errors':  str(form.errors),'status':'not_ok'}
			return JsonResponse(response_data)
	else:
		form=AddPaypal()
		print("app has gone crazy")
		return render(request,'passenger/chooseTicket.html')	
	pass
		
def buyMultipleTickets(request):
	cus_id=request.session["username"]
	if request.method== "GET":
		form=BuyMultiplePasses()
		return render (request,'passenger/buyMultipleTickets.html',{'form':form})
	#add card online and in local db
	elif request.method=="POST" and request.is_ajax:
		form= BuyMultiplePasses(data=request.POST)
		tickets_dict=dict()
		invoice=dict()
		total_passengers=0
		destination="Nyahururu"
		if form.is_valid():
			children_number = request.POST["children_number"];
			adult_number = request.POST["adult_number"];
			passenger_id = request.POST["passenger_id"];
			type_1_ticket = request.POST["type_1_ticket"];
			type_2_ticket = request.POST["type_2_ticket"];
			type_3_ticket = request.POST["type_3_ticket"];
			type_4_ticket = request.POST["type_4_ticket"];
			type_5_ticket = request.POST["type_5_ticket"];
#search for the empty and full ones.
			if type_1_ticket == "Type1":
				tickets_dict["Type1"]="Type1"
			if type_2_ticket == "Type2":	
				tickets_dict["Type2"]="Type2"
			if type_3_ticket == "Type3":
				tickets_dict["Type3"]="Type3"
			if type_4_ticket == "Type4":
				tickets_dict["Type4"]="Type4"
			if type_5_ticket == "Type5":
				tickets_dict["Type5"]="Type5"
			if children_number != None:
				total_passengers = total_passengers+children_number
			if adult_number != None:
				total_passengers =total_passengers +children_number
			if passenger_id != None:
				total_passengers = total_passengers +1
			amount_cost=calculate_cost(tickets_dict,pass_num,destination)
			invoice["amount_cost"]=amount_cost
			invoice["total_passengers"]=total_passengers
			invoice["tickets_dict"]=tickets_dict
			customer_id=""#from session
			#createCharge(amount,customer_id,card_id,payment_method)

			print("children_number")
			print(children_number)
			print("adult_number")
			print(adult_number)
			print("passenger_id")
			print(passenger_id)
			
			response_data = {'received': True, 'errors':  str(form.errors),'status':'ok'}
			return JsonResponse(response_data)
		else:
			print("formerrors")
			print(form.errors)
			response_data = {'received': False, 'errors':  str(form.errors),'status':'not_ok'}
			return JsonResponse(response_data)
	else:
		form=AddPaypal()
		print("app has gone crazy")
		return render(request,'passenger/chooseTicket.html')	
	pass
def calculate_cost(tickets_dict,destination, pass_num=1 ):

	return 270
def buySingleTickets(request):
	pass
def giveUserTickets(request,token):
	#record tickets for the necessary people
	#retrieve
	pass
def addBankAccounts(request,token):
	#verify bank manually and store it locally and online
	# use plaid or verify manually
	pass
def updateBankAccount(request,account_id):
	pass
def deleteBankAccount(request,account_id):
	pass
def addPaypal(request):
	cus_id=request.session["username"]
	#verify paypal account and store details online
	if request.method== "GET":
		form=AddPaypal()
		return render(request,'passenger/addEmail.html', {'form':form})
	#add card online and in local db
	elif request.method=="POST" and request.is_ajax:
		form= AddPaypal(data=request.POST)
		if form.is_valid():
			email = request.POST["email"];
			response_data = {'received': True, 'errors':  str(form.errors),'status':'ok',}
			return JsonResponse(response_data)
		else:
			print("formerrors")
			print(form.errors)
			response_data = {'received': False, 'errors':  str(form.errors),'status':'not_ok'}
			return JsonResponse(response_data)
	else:
		form=AddPaypal()
		return render(request,'passenger/addEmail.html')


	#store card locally	
	#populate addcard
	pass
def getbalance(request,token,customer_id,balance_id):
	pass
def getCharge(request,charge_id,customer_id):
	pass
def getCustomerDetails(request,customer_id):
	pass
def webhooks_manager(request):
	pass
def dispute_handling(request):
	#any disputes handling
	#handle frauds
	pass
def refund(request):
	pass

