from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('axisPosts.urls')),
    path('base/', include('axisCore.urls')),
    path('users/', include('axisUsers.urls')),
    path('pms/',include('axisPMS.urls')),
    path('admin/', admin.site.urls),
]
