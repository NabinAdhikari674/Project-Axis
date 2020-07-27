from django.contrib import admin

from .models import Awards,User
# Register your models here.

#admin.site.register(Awards)
#admin.site.register(User)

class UserViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','date_joined')
    list_filter = ("date_joined","country")
    search_fields = ['username', 'email','first_name','last_name']
    #prepopulated_fields = {'slug': ('title',)}
class AwardsViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'awardId', 'award','count')
    list_filter = ("id","award","count")
    search_fields = ['award', 'count','awardId','id']

admin.site.register(User, UserViewAdmin)
admin.site.register(Awards, AwardsViewAdmin)
