# axisCore
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import uploadPost
from django.contrib import messages

def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)

def uploadPostFormView(request):
    uploadPostForm = uploadPost()
    context = {'uploadPostForm':uploadPostForm}
    return render(request, 'axisCore/uploadPost.html', context)

def uploadPostonDB(request):
    if request.method == "POST":
        uploadPostForm = uploadPost(request.POST)
        if uploadPostForm.is_valid():
            userData = uploadPostForm.save(commit=False)
            #userPass = form.cleaned_data['password']
            #userData.set_password(userPass)
            #userData.save()
            return ("<p>Post Saved !!!</p>")
        else:
            messages.error(request,"Invalid Input. Please Correctly Fill all Required Fields.")
    return JsonResponse({'foo': 'bar'})
