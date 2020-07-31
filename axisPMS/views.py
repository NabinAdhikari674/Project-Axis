from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader


def pmsPostView(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'pms':'pms'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisPMS/pms.html', context)
