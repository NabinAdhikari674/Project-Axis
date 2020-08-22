from . import views
from django.urls import path

app_name = 'axisPMS' # NameSpace for app

urlpatterns = [
    path('', views.pmsPostView, name='pmsPostView'),
    path('search/',views.searchPost,name='search'),
    path ('pmssearch',views.pmsSearch,name='pmsSearch'),
    path ('sort',views.sort,name='sort'),
]
