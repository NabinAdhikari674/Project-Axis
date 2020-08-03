# axisCore
from django.shortcuts import render
#from django.http import HttpResponse
from django.http import JsonResponse
from .forms import uploadPostForm
#from django.contrib import messages
from django.contrib.auth.decorators import login_required

def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)
@login_required
def uploadPostFormView(request):
    PostForm = uploadPostForm()
    context = {'uploadPostForm':PostForm}
    return render(request, 'axisCore/uploadPost.html', context)
@login_required
def uploadPostonDB(response):
    if response.method == "POST":
        form = uploadPostForm(response.POST)
        if form.is_valid():
            form.cleaned_data['postAuthor'] = response.user
            form.save()
            return JsonResponse({'Form':"SAVED"})
        else:
            return JsonResponse({'Form':"Not Valid"})
    else:
        return JsonResponse({'POST':"NOT VALID"})
    return JsonResponse({'Request':"Invalid Request"})
