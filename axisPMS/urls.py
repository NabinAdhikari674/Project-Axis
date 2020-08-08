from . import views
from django.urls import path

app_name = 'axisPMS' # NameSpace for app

urlpatterns = [
<<<<<<< HEAD
    path('', views.pmsPostView, name='pmsPostView'),
=======
    path('', views.pmsPostView, name='pmspostView'),
    path('search/',views.searchPost,name='searchPost'),
>>>>>>> 290b4483408d4ccdd934886299cddb77f92a3266
]
