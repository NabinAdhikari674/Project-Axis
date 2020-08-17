from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.core import serializers
#from django.template import loader
from .forms import RegisterUser,LoginUser,userProfile
from .models import User,userAwards

def login_request(request):
    #template = loader.get_template('axisUsers/login.html')
    if request.method == "POST":
        form = LoginUser(request=request, data=request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            userPass = form.cleaned_data.get('password')
            user = authenticate(username=userName, password=userPass)
            if user is not None :
                login(request, user)
                print("logged In")
                messages.info(request,f"You are Logged In as : {userName}")
                return redirect("axisPosts:postView")
            else :
                #return redirect("../../")
                messages.error(request,"Invalid Username Or Password")
        else :
            #return redirect("axisUsers:register")
            messages.error(request,"Invalid Input")
    form = LoginUser()
    return render (request,'axisUsers/login.html',{'form':form})

def logout_request(request):
    logout(request)
    #messages.info(request, "Logged out successfully!")
    return redirect("axisPosts:postView")

def register(response):
    #template = loader.get_template('axisUsers/register.html')
    if response.method == "POST":
        form = RegisterUser(response.POST)
        if form.is_valid():
            userData = form.save(commit=False)
            userPass = form.cleaned_data['password']
            userData.set_password(userPass)
            userData.save()
            return redirect("../login/")
        else:
            messages.error(response,"Invalid Input. Please Correctly Fill all Required Fields.")
    else:
        form = RegisterUser()
    return render(response,'axisUsers/register.html',{"form":form})

def viewProfile(response):
    #model = User.objects.all()
    context = {'model':'model','app_name':"axisUsers",'noSettingSidebar':True}
    return render(response,'axisUsers/profile.html',context)

def terms(request) :
    #template = loader.get_template('axisUsers/terms.html')
    context = {'terms':'termsAndConditions'}
    return render(request,'axisUsers/terms.html',context)

def updateUserProfile(response) :
    if response.method == "POST":
        form = userProfile(response.POST)
        if form.is_valid():
            userDetails = User.objects.get(id=response.user.id)
            profileUsername = form.cleaned_data['username']
            profileEmail = form.cleaned_data['email']
            profilePhone = form.cleaned_data['phone']
            if profileUsername != getattr(userDetails, 'username'):
                if (uniqueUsernameValidation(profileUsername)):
                    userDetails.username = profileUsername
                else :
                    return JsonResponse({'Error-username':'That Username Is Already Taken'})
            if profileEmail != getattr(userDetails, 'email'):
                if (uniqueEmailValidation(profileEmail)):
                    userDetails.email = profileEmail
                    userDetails.emailConfirmed = False
                else :
                    return JsonResponse({'Error-email':'That Email Already Has An Account in Axis'})
            if profilePhone != getattr(userDetails, 'phone'):
                if (uniqueNumberValidation(profileEmail)):
                    userDetails.phone = profilePhone
                    userDetails.phoneConfirmed = False
                else :
                    return JsonResponse({'Error-number':'That Number Already Has An Account in Axis'})
            userDetails.first_name = form.cleaned_data['first_name']
            userDetails.last_name = form.cleaned_data["last_name"]
            userDetails.gender = form.cleaned_data["gender"]
            userDetails.country = form.cleaned_data["country"]
            userDetails.state = form.cleaned_data["state"]
            userDetails.city = form.cleaned_data["city"]
            userDetails.area = form.cleaned_data["area"]
            userDetails.save()      
            #data = serializers.serialize('json', [ user_details, ])
            return JsonResponse({'Profile':'UPDATED'})
        else:
            return JsonResponse({'Error-Form':form.errors})

    else:
        return JsonResponse({'Error-POST':'POST Request Not Valid'})

def uniqueUsernameValidation(request):
    if (User.objects.filter(username__iexact=request).exists()):
        return False
    else:
        return True
def uniqueEmailValidation(request):
    if (User.objects.filter(email__iexact=request).exists()):
        return False
    else:
        return True
def uniqueNumberValidation(request):
    if (User.objects.filter(phone__iexact=request).exists()):
        return False
    else:
        return True

'''
def validate_username(request):
    username = request.POST.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
def validate_email(request):
    email = request.POST.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
'''