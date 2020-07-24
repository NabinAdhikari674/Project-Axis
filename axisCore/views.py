# axisCore
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('axisCore/index.html')
    context = {'main':'main'}
    return HttpResponse(template.render(context,request))
    #return HttpResponse("Hello. Welcome, You're at the AxisCore index.")

# Create your views here.
