##################forms used for authentication#####################
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from authetr.models import Users
from django.contrib.auth.hashers import make_password
#REGISTRATION
#registration email and password
def validate_my_email(email):
	try:
		Users.objects.get(email=email)
		raise forms.ValidationError(("The email you used already exists"))
	except Users.DoesNotExist:
		try:
			validate_email(email)
			return email
		except forms.ValidationError:
			print("not any errors")
			raise forms.ValidationError(("Your email is invalid"))

def validate_password_strength(password):
	#length and regex
	pass
def validate_contact_length(phone_number):
	#try:
		#User.objects.get(contact=phone_number)
	#except User.DoesNotExist:
		#if len(phone_number) < 10:
			#raise forms.ValidationError(_("Invalid Cellphone"))
			#return phone_number
		#else:
			#raise forms.ValidationError(_("Phone already registered"))
	pass

class RegistrationForm(forms.Form):
	name =forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control '}), label="Your Name")
	contact= forms.DecimalField(widget=forms.NumberInput(attrs={}),label="contact info.",validators=[validate_contact_length])
	email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control '}), label="Email", validators=[validate_my_email])
	password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}), label="Password",  validators=[validate_password_strength])
	password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}), label="Confirm Password", validators=[validate_password_strength])
	
#facebook
#twitter
#google
class ActivationConfirm(forms.Form):
	activation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control '}), label="")
class AddContact(forms.Form):
	contact= forms.DecimalField(widget=forms.NumberInput(attrs={}),label="contact info.",validators=[validate_contact_length])
class ChangePass(forms.Form):
	old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}, render_value=False), label="Old Password",  validators=[validate_password_strength])
	new_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}, render_value=False), label="New Password",  validators=[validate_password_strength])
	new_password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}), label="Confirm Password", validators=[validate_password_strength])
class AddEmail(forms.Form):
	add_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control '}), label="Email", validators=[validate_my_email])
class ForgotPass(forms.Form):
	new_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}, render_value=False), label="New Password", validators=[validate_password_strength])
	new_password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}), label="Confirm Password", validators=[validate_password_strength])	
#LOGINN
class Loginn(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control '}), label="Email", validators=[validate_my_email])
	password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control '}), label="Password", validators=[validate_password_strength])