# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = 'axisUsers'

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
    path('update/', views.updateUserProfile, name='updateUserProfile'),
    path('profile/', views.viewProfile, name='profile'),
    path('terms/', views.terms, name='termsAndConditions'),
    
]
