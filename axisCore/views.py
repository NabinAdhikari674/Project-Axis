# axisCore
from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import JsonResponse

#from django.contrib import messages

def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)