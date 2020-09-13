from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'axisPosts' # NameSpace for app

urlpatterns = [
    path('', views.postView, name='postView'),
    path('postForm/', views.uploadPostFormView, name='uploadPostFormView'),
    path('uploadPost/', views.uploadPostonDB, name='uploadPostonDB'),
    path('postDetailView/', views.postDetailView, name='postDetailView'),
    path('reactions/', views.reactions, name='reactions'),
    path('postNewComment/', views.postNewComment, name='postNewComment'),
    path('posts/', views.userPosts, name='userPosts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
