from django.core.paginator import Paginator
from django.shortcuts import render
#from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.template import loader
from .forms import uploadPostForm
from .models import Post,postReactions,postComments,commentReactions
from axisUsers.models import User

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

@login_required
def uploadPostFormView(request):
    return render(request, 'axisPosts/uploadPost.html', {'uploadPostForm':uploadPostForm()})
@login_required
def uploadPostonDB(response):
    if response.method == "POST":
        form = uploadPostForm(response.POST,response.FILES)
        if form.is_valid():
            form.cleaned_data['postAuthor'] = response.user
            newPost = form.save(commit=False)
            newPost.save()
            return JsonResponse({'Form':"SAVED"})
        else:
            return JsonResponse({'Error':True,'Errors':form.errors})
    else:
        form = uploadPostForm()
    return render(response, 'axisPosts/uploadPost.html',{'uploadPostForm':form})
    

def postDetailView(request):
    if request.method == 'GET':
        postId = request.GET.get('postId',None)
        post = Post.objects.get(id=postId)
        if request.user.is_authenticated:
            try:
                postRc = postReactions.objects.get(postId=postId,userName=request.user)
            except:
                postRc=[]
        else :
            postRc =[]
        try :
            postCmts = postComments.objects.filter(postId=postId).order_by('-popularity')
        except exp as Exception:
            postCmts = []
            #print(exp)
        #print("Post Reaaction iS : ",postRc.reaction)
        context = {'post':post,'reactions':postRc,'comment_feed':postCmts}
        return render(request, 'axisPosts/postDetail.html', context)

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

@login_required
def postNewComment(request):
    if request.method == 'GET':
        pid = request.GET.get('pid',None)
        cmt = request.GET.get('cmt',None)
        cid = request.GET.get('cid',None)
        if cmt:
            newCmt = postComments.objects.create(postId=Post(id=pid),parentId=postComments(id=cid),commentAuthor=request.user,comment=cmt)
            if (newCmt.id):
                context = {"comment":newCmt}
                return render(request, 'axisPosts/comment.html',context)
            else:
                return JsonResponse({'Comment':"Comment Upload Error"})
        else :
            return JsonResponse({'Comment':"Empty Comment Error"})