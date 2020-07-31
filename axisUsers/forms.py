from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class RegisterUser(forms.ModelForm):
    username = forms.CharField(label='username',required=True,
                                help_text='Your Username for Axis',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email',required=True,
                                help_text='Your Email for Axis',
                                widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Password',max_length=32,min_length=6,required=True,
                                help_text='A Strong Password has Combination of Letters,Numbers and Characters',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    phone = forms.IntegerField(label='Phone',required=False,
                                widget=forms.NumberInput(attrs={'placeholder': 'Phone Number'}))
    genderChoices = [('ML', 'Male'),('FM', 'Female'),('O', 'Other')]
    gender = forms.ChoiceField (label='Gender',required=False,
                                widget=forms.RadioSelect(attrs={'title': 'Gender'}),choices=genderChoices)
    first_name = forms.CharField(label='FirstName',max_length=20,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='LastName',max_length=20,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    country = forms.CharField(label='Country',max_length=20,required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    state = forms.CharField(label='State',max_length=20,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'State (If Applicable)'}))
    city = forms.CharField(label='City',max_length=20,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'City'}))
    area = forms.CharField(label='Area',max_length=20,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Area (Local Area Name)'}))

    class Meta:
    	model = User
    	fields = ["first_name","last_name","email","username","password","gender","country"]

class LoginUser(AuthenticationForm):
    username = forms.CharField(label='username',required=True,
                                help_text='Your Username for Axis',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',max_length=32,min_length=6,required=True,
                                help_text='A Strong Password has Combination of Letters,Numbers and Characters',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ["username","password"]
