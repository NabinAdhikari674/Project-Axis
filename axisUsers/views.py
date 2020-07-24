from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def login(request):
    template = loader.get_template('axisUsers/login.html')
    context = {'main':'main'}
    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('axisUsers/register.html')
    context = {'main':'main'}
    return HttpResponse(template.render(context,request))
