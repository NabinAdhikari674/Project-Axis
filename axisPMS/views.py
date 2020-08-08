from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import pmsPost


def pmsPostView(request):
    #template = loader.get_template('axisPMS/sort.html')
    context = {'sort':'sort'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisPMS/pms.html', context)

def searchPost(request):
    if request.method == "GET":
        searchQuery=request.GET
        data = pmsPost.objects.filter(projectTitle__icontains=searchQuery)
        return render(request,"axisPMS/search.html", {'data': data})
    return render(request,"axisPMS/search.html", {'data': 'data'})
            
   
       

   
                

