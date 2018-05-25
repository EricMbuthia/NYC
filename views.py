from django.shortcuts import render,redirect
from authetr.forms import RegistrationForm, Loginn, ActivationConfirm
from django.contrib import auth;
from django.http import JsonResponse
from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.core.mail import send_mail
import stripe
from authetr.models import Users
SEC_KEY = settings.SECRET_STRIPE_KEY
stripe.api_key=SEC_KEY
authy_api=settings.AUTHY_API_KEY
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
#load registrattion page
def registration(request):
	form= RegistrationForm()
	form2=ActivationConfirm()
	return render(request, "authetr/register.html",{'form':form,'form2':form2});
#receive data from registration page	
def register(request):
	if request.method == "POST" and request.is_ajax:
		form= RegistrationForm(data=request.POST)
		if form.is_valid():
			name = request.POST["name"];
			email = request.POST["email"];
			contact = request.POST["contact"];
			password = request.POST["password"]
			print("first pass")
			print(password)
			#username = request.POST["user_name"];
			#password = request.POST["password"];
			#email = request.POST["email"];
			#phone_number=request.POST["phone_number"]
			#send confirmation email and also phone
			#send_mail( 'Subject here','Here is the message.', 'from@example.com',['to@example.com'],fail_silently=False,)
			user = authy_api.users.create(email, contact, 254) #email, cellphone, country_code
			request.session['name'] = name
			request.session['email'] = email
			request.session['contact'] = contact
			request.session['password'] = password
			if user.ok():
				user_authy_id=user.id
				sms=authy_api.users.request_sms(user_authy_id)
				if sms.ok():
					request.session['authy_id'] = user_authy_id
					response_data = {'sms_sent': True, 'errors': "none",'status':'ok'}
					return JsonResponse(response_data)	


			#send confirmation email and also phone
			#send_mail( 'Subject here','Here is the message.', 'from@example.com',['to@example.com'],fail_silently=False,)
	        # call create_user from the ORM. Make sure you call save!

			#auth.models.User.objects.create_user(username, email, password).save();
	        #log the user in
			#user = auth.authenticate(username = username, password = password);
			#auth.login(request, user);
			#print("logged in")
			
		else:
			print("formerrors")
			print(form.errors)
			response_data = {'form_saved': False, 'errors': str(form.errors)}
			#go to finance details
			return JsonResponse(response_data)#,safe=False)


#log in user after they fill form
def verify(request):
	if request.method == "POST" and request.is_ajax:
		form=  ActivationConfirm(data=request.POST)
		if form.is_valid():	
			activation= request.POST["activation"]	
			authy_id=request.session['authy_id']
			verification = authy_api.tokens.verify(authy_id, activation)
			if verification.ok():
				email=request.session['email']
				name=request.session['name']
				contact=request.session['contact']
				password=request.session['password']#make_password(password=request.session["password"])
				print("Second Plain password")
				print(password)
				description="Account for "+ email
				customer=stripe.Customer.create(description=description,email=email)
				print("customer id")
				customer_id=customer.id
				print(customer.id)
				user=auth.models.User.objects.create_user(customer_id, email, password).save();
				user_save=Users(name=name,email=email,contact=contact,password=password,customer_id=customer_id,authy_id=authy_id)
				user_save.save()
				user = auth.authenticate(email= email, password = password);
				print("verify after authenticate")
				response_data = {'logged_in': True, 'errors': "none",'status':'ok'}
				return render(request, "passenger/home.html");
			else:
				print("wrong code")
		else:
			print("form errors")
	pass
def login(request):
	print("user is logged in and username is ")
	print(request.user.username)
		


	form=Loginn()
	if request.method == "GET":
		print("look form")
		return render(request, "authetr/login.html",{'form':form});
	elif request.method == "POST" and request.is_ajax:
		#never mind about this line its a form of test
		print("inposttttt")
		email = request.POST['email'];
		print("email")
		print(email)
		password = request.POST['password'];#make_password(password=request.POST["password"])#
		#password = cleaned_data["password"]
		print("un login hashed password ")
		print(password)

		try:
			user_retrieve=User.objects.get(email=email)
			print("user_retrieve password ")
			print(user_retrieve.password)
			print("user_retrieve username ")
			print(user_retrieve.username)
			# make sure the username & password is good
			user = auth.authenticate(username=user_retrieve.username, password=password);

			if user is not None: # User was found & password matched
				if user.is_active:
				#associate the user with the session
					print("auth about to happen")
					auth.login(request, user);
					print("auth after to happen with username as")
					print(request.user.username)
					request.session['username']=request.user.username
					return render(request, "passenger/home.html");
				else:
					print("acount disabled")
			#read the destination
					#next = "";
					#if "next" in request.GET:
						#next = request.GET["next"];
					#if next == None or next == "":
						#next = "/";
						#return redirect(next);
			else:
				# bad username and password
				print("bad username and pass")
				return render(request, "authetr/login.html", { "warning": "Invalid username and or password" });
		except User.DoesNotExist as e:
			print("User DoesNotExist"+ str(e))
			return render(request, "authetr/login.html", { "warning": "Invalid username and or password" });

			