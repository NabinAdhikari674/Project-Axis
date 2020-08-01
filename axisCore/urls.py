# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = "axisCore"
urlpatterns = [
    path('', views.base, name='base'),
    path('uploadPost/', views.uploadPostFormView, name='uploadPostFormView'),
]
