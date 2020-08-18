from django.core.paginator import Paginator
from django.shortcuts import render
#from django.views import generic
from django.http import JsonResponse
#from django.http import HttpResponse
#from django.template import loader
from .models import Post,postReactions
from axisUsers.models import User 
#from .models import postComments,commentReactions
from django.contrib.auth.decorators import login_required


def postView(request):
    model = Post.objects.all()
    postPG = Paginator(model, 10)
    firstPage = postPG.get_page(1)
    #pageRange = postPG.page_range
    postIds = [x.id for x in firstPage]
    if request.user.is_authenticated:
        postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
    else :
        postRcs =[]
    app = 'axisPosts'
    context = {'post_list': firstPage,'reaction_list':postRcs,'page_n':1,'app_name':app}

    if request.method == 'POST':
        page_n = int(request.POST.get('page_n', None))
        page_n += 1
        results = postPG.get_page(page_n)
        postIds = [x.id for x in results]
        if request.user.is_authenticated:
            postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
        else :
            postRcs =[]
        context = {'post_list': results,'reaction_list':postRcs,'page_n':page_n}
        return render(request, 'axisPosts/postList.html',context) 

    return render(request,'axisPosts/post.html',context) 

def postViewTest1(request):
    post_list = Post.objects.order_by('-popularity')
    context = {'post_list':post_list}
    return render(request, 'axisPosts/post.html', context)
@login_required
def reactions(request):
    if request.method == 'POST':
        postId = request.POST.get('postId',None)
        userRec = int(request.POST.get('reaction',None))
        try:
            postObj = Post.objects.get(id=postId)
        except Post.DoesNotExist:
            return JsonResponse({'Alert':"Post NOT FOUND"})
        try:
            reactionObj = postReactions.objects.get_or_create(postId=Post(id=postId),userName=User(id=request.user.id),defaults={'reaction': 0})
        except postReactions.MultipleObjectsReturned:
            postReactions.objects.filter(postId=postId,userName=request.user).delete()
            reactionObj = postReactions.objects.create(postId=Post(id=postId),userName=User(id=request.user.id),defaults={'reaction': 0})
        if userRec == 1:
            if (reactionObj[0].reaction == 2):
                 postObj.popularity += 1
            if (reactionObj[0].reaction == 1):
                reactionObj[0].reaction = 0
                postObj.popularity -= 1
                popuCounter = postObj.popularity
                postObj.save()
                reactionObj[0].save()
                return JsonResponse({'Reaction':"Updated",'Counter':popuCounter})
            else:
                reactionObj[0].reaction = 1
                postObj.popularity += 1
                popuCounter = postObj.popularity
                postObj.save()
                reactionObj[0].save()
                return JsonResponse({'Reaction':"Upped",'Counter':popuCounter})
        elif userRec == 2:
            if (reactionObj[0].reaction == 1):
                 postObj.popularity -= 1
            if (reactionObj[0].reaction == 2):
                reactionObj[0].reaction = 0
                postObj.popularity += 1
                popuCounter = postObj.popularity
                postObj.save()
                reactionObj[0].save()
                return JsonResponse({'Reaction':"Updated",'Counter':popuCounter})
            else:
                reactionObj[0].reaction = 2
                postObj.popularity -= 1
                popuCounter = postObj.popularity
                postObj.save()
                reactionObj[0].save()
                return JsonResponse({'Reaction':"Down",'Counter':popuCounter})

   