from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegisterUser
from .models import User

def login(request):
    template = loader.get_template('axisUsers/login.html')
    context = {'main':'main'}
    return HttpResponse(template.render(context,request))

def register(response):
    #template = loader.get_template('axisUsers/register.html')
    if response.method == "POST":
    	form = RegisterUser(response.POST)
    	if form.is_valid():
            #form = form.save(commit=False)
            #form.user = response.POST.Username
            form.save()
            return redirect("../login/")
    else:
        form = RegisterUser()
    return render(response,'axisUsers/register.html',{"form":form})

def terms(request) :
    template = loader.get_template('axisUsers/terms.html')
    context = {'main':'main'}
    return HttpResponse(template.render(context,request))
