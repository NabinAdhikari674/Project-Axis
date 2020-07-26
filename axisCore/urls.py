# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = "axisCore"
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/axisCore/favicon.ico'))
]
