##################forms used by passengers#####################
from django import forms
from django.core import validators

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from django.contrib import auth;

from authetr.models import Users
def validate_driver_id(driver_id):
	#check in db
	pass
def validate_maxlength3(field):
	pass
def validate_my_email(email):
	pass
def validate_username(user_name):
    ##try:
       # user=User.objects.get(username=user_name)
        #if User.objects.filter(username=user_name).exists():
            #print("errorsfound")
    #except User.DoesNotExist:
     #   print("no errors")
      #  if len(user_name) < 3:
       #     raise forms.ValidationError(("Invalid Username"))
       # return user_name
    pass
   


def validate_phone(phone_number):
    if len(phone_number) < 10:
        raise forms.ValidationError(("Invalid Cellphone"))
    return phone_number
        
    

def validate_my_email(email):
    try:
        Users.objects.get(email=email)
        raise forms.ValidationError(("Email already registered"))
    except Users.DoesNotExist:
        try:
            validate_email(email)
            return email
        except forms.ValidationError:
            print("not any errors")
            raise forms.ValidationError(("Email Invalid"))

    

def validate_password_strength(value):
    """Validates that a password is as least 7 characters long and has at least
    1 digit and 1 letter.
    """
    min_length = 8

    if len(value) < min_length:
        raise ValidationError(('Password must be at least {0} characters '
                                'long.').format(min_length))

    # check for digit
    if not any(char.isdigit() for char in value):
        raise ValidationError(('Password must contain at least 1 digit.'))

    # check for letter
    if not any(char.isalpha() for char in value):
        raise ValidationError(('Password must contain at least 1 letter.'))
# Add card
def check_char(value):
    """Validates that a password is as least 7 characters long and has at least
    1 digit and 1 letter.
    """
    # check for letter
    if any(char.isalpha() for char in value):
        raise ValidationError(('Value cannot contain alphabets only numeric.'))
def validate_passenger_id(pass_id):
    #check from db if they are valid
    pass
    
# Add card
class AddCard(forms.Form):
	name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control required','name':'name' }), label="Your Name")
	card_number= forms.CharField(max_length=20,widget=forms.TextInput( attrs={'class':"card-number stripe-sensitive required"}),label="Card Number")
	cvc= forms.CharField(max_length=4,widget=forms.TextInput(attrs={ 'class':'card-cvc stripe-sensitive required'}),label="Card CVC")
	email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control required','name':'email'}), label="Email", validators=[validate_my_email])
	expiry_date=forms.DateField(widget=forms.DateInput) #change to stripe select

#Add Paypal
class AddPaypal(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control '}), label="Email", validators=[validate_my_email])
#Add bank
class AddBank(forms.Form):
	bank_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control '}), label="Bank Name")
	bank_account_number= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control '}), label="Account Number")
	bank_location=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control '}), label="Your Bank Location")
#pay by card

#pay by paypal
#Multiple Tickets
class BuyMultiplePasses(forms.Form):
    CHOICES=(('Type1','Type1',),('Type2','Type2',),('Type3','Type3',),('Type4','Type4',),('Type5','Type5',),)
    type_1_children_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Children for Type1",validators=[check_char])
    type_1_adult_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Adults  for Type1",validators=[check_char])
    type_2_children_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Children for Type2",validators=[check_char])
    type_2_adult_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Adults for Type2",validators=[check_char])
    type_3_children_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Children for Type3",validators=[check_char])
    type_3_adult_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Adults for Type3",validators=[check_char])
    type_4_children_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Children for Type4",validators=[check_char])
    type_4_adult_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Adults for Type4",validators=[check_char])
    type_5_children_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Children for Type5",validators=[check_char])
    type_5_adult_number= forms.CharField(required=False,max_length=3,widget=forms.TextInput(attrs={'class':'col-lg-6 col-md-6'}),label="Number of Adults for Type5",validators=[check_char])
    
    passenger_id = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={}), label="NYC Id",validators=[validate_passenger_id])
    type_1_ticket=forms.CharField( required=False,widget=forms.CheckboxInput(attrs={'value':'Type1'}), label="Type 1")#, choices=CHOICES)
    type_2_ticket=forms.CharField( required=False,widget=forms.CheckboxInput(attrs={'value':'Type2'}), label="Type 2")#, choices=CHOICES)
    type_3_ticket=forms.CharField( required=False,widget=forms.CheckboxInput(attrs={'value':'Type3'}), label="Type 3")# ,choices=CHOICES)
    type_4_ticket=forms.CharField( required=False,widget=forms.CheckboxInput(attrs={'value':'Type4'}), label="Type 4")#, choices=CHOICES)
    type_5_ticket=forms.CharField(required=False,widget=forms.CheckboxInput(attrs={'value':'Type5'}), label="Type 5")#, choices=CHOICES)

    # Submit Button should be made inactive on pressing


#Single Ticket
class BuySinglePasses(forms.Form):
    CHOICES=(('Type1','Type1',),('Type2','Type2',),('Type3','Type3',),('Type4','Type4',),('Type5','Type5',),)
    type_1_ticket=forms.ChoiceField(required=False, widget=forms.CheckboxInput(attrs={'value':'Type1'}), label="Type 1", choices=CHOICES)
    type_2_ticket=forms.ChoiceField(required=False, widget=forms.CheckboxInput(attrs={'value':'Type2'}), label="Type 2", choices=CHOICES)
    type_3_ticket=forms.ChoiceField(required=False, widget=forms.CheckboxInput(attrs={'value':'Type3'}), label="Type 3" ,choices=CHOICES)
    type_4_ticket=forms.ChoiceField(required=False, widget=forms.CheckboxInput(attrs={'value':'Type4'}), label="Type 4", choices=CHOICES)
    type_5_ticket=forms.ChoiceField(required=False, widget=forms.CheckboxInput(attrs={'value':'Type5'}), label="Type 5", choices=CHOICES)

    # Submit Button should be made inactive on pressing

#Pay Through Id
class PayById(forms.Form):
	driver_id= forms.CharField(max_length=20,widget=forms.TextInput(attrs={}),label="Driver Id")

#pay through scanning a code
#class PayByQr(forms.Form):
