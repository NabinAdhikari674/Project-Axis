# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = "axisCore"
urlpatterns = [
    path('', views.base, name='base'),
    path('postForm/', views.uploadPostFormView, name='uploadPostFormView'),
    path('uploadPost/', views.uploadPostonDB, name='uploadPostonDB'),
]
