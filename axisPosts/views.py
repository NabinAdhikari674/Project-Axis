from django.core.paginator import Paginator
from django.shortcuts import render
#from django.views import generic
#from django.http import HttpResponse
#from django.template import loader
from .models import Post
#from .models import postComments,postReactions,commentReactions


def postView(request):
    model = Post.objects.all()
    postPG = Paginator(model, 10)
    firstPage = postPG.get_page(1)
    #pageRange = postPG.page_range
    app = 'axisPosts'
    context = {'post_list': firstPage,'page_n':1,'app_name':app}

    if request.method == 'POST':
        page_n = int(request.POST.get('page_n', None))
        page_n += 1
        results = postPG.get_page(page_n)
        context = {'post_list': results,'page_n':page_n}
        return render(request, 'axisPosts/postList.html',context) 

    return render(request,'axisPosts/post.html',context) 

def postViewTest1(request):
    post_list = Post.objects.order_by('-popularity')
    context = {'post_list':post_list}
    return render(request, 'axisPosts/post.html', context)