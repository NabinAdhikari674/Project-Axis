from . import views
from django.urls import path

app_name = 'axisPosts' # NameSpace for app

urlpatterns = [
    path('', views.postView, name='postView'),
    path('postDetail/', views.postDetail, name='postDetail'),
]
