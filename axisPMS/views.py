from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import pmsPost
from axisPosts.models import Post
import datetime
from django.db.models import Q

def pmsPostView(request):
    #template = loader.get_template('axisPMS/sort.html')
    app = 'axisPMS'
    context = {'sort':'sort','app_name':app}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisPMS/pms.html', context)

def searchPost(request):
    if request.method == "GET":
        searchQuery=request.GET.get('searchQuery','gautam')
        print(searchQuery,"miss you search")
        data = Post.objects.filter(postTitle__icontains=searchQuery)
        return render(request,"axisPMS/search.html", {'data': data})


            
   
def pmsSearch(request):
     if request.method == "GET":
        searchQuery=request.GET.get('searchQuery',fd)
        result = City.objects.filter(Q(projectTitle__icontains=fd) | Q(category__icontains=fd)/Q(status__icontains=fd))
        return render(request,"axisPMS/pmsSearch.html", {'result': result})


def sort(request):
    now = datetime.datetime.now()
    date=pmsPost.objects.all.order_by(now,createdOn)
    return render(request,"axisPMS/sort.html", {'date': date})

            
                   

   
                
  
