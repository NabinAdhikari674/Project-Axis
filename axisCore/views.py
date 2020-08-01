# axisCore
from django.shortcuts import render
from .forms import uploadPost
#from django.http import HttpResponse
#from django.template import loader


def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)

def uploadPostFormView(request):
    #uploadPostForm = uploadPost()
    #context = {'uploadPostForm':uploadPostForm}
    context = {'form':'form'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/uploadPost.html', context)
