from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from .models import Post,postComments,postReactions,commentReactions

# Create your views here.
class PostList(generic.ListView):
    post_list = Post.objects.order_by('-popularity')
    #template = loader.get_template('axisPosts/post.html')
    #template = 'post.html'
    context = {'post_list':post_list}
    #return HttpResponse(template.render(context,request))

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'postDetail.html'

def postView(request):
    post_list = Post.objects.order_by('-popularity')
    #template = loader.get_template('axisPosts/post.html')
    #template = 'post.html'
    context = {'post_list':post_list}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisPosts/post.html', context)
def postDetail(request):
    post_list = Post.objects.order_by('-popularity')
    #template = loader.get_template('axisPosts/postDetail.html')
    #template = 'post.html'
    context = {'post_list':post_list}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisPosts/postDetail.html', context)
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
