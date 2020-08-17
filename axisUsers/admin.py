from django.contrib import admin

from .models import User,axisAwards,userAwards
# Register your models here.

#admin.site.register(Awards)
#admin.site.register(User)

class UserViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','date_joined')
    list_filter = ("date_joined","country")
    search_fields = ['username', 'email','first_name','last_name']
    #prepopulated_fields = {'slug': ('title',)}
class UserAwardsViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'awardId','user','count')
    list_filter = ("awardId",'user',"count")
    search_fields = ['awardId', 'count','user']
class AxisAwardsViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'awardName','awardType', 'awardDesc')
    list_filter = ("awardName","awardType")
    search_fields = ['awardName','awardType']

admin.site.register(User, UserViewAdmin)
admin.site.register(axisAwards, AxisAwardsViewAdmin)
admin.site.register(userAwards, UserAwardsViewAdmin)