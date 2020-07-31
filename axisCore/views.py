# axisCore
from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader


def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)


def uploadPost(request):
    context = {'post':'axisPOST'}
    return render(request,'axisCore/uploadPost.html',context)
