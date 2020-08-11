from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
#from django.template import loader
from .forms import RegisterUser,LoginUser
from .models import User,Awards

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

'''
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
'''
