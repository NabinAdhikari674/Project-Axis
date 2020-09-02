from django.urls import path
from . import views

app_name = 'axisPosts' # NameSpace for app

urlpatterns = [
    path('', views.postView, name='postView'),
    path('postForm/', views.uploadPostFormView, name='uploadPostFormView'),
    path('uploadPost/', views.uploadPostonDB, name='uploadPostonDB'),
    path('postDetailView/', views.postDetailView, name='postDetailView'),
    path('reactions/', views.reactions, name='reactions'),
    path('postNewComment/', views.postNewComment, name='postNewComment'),
]
