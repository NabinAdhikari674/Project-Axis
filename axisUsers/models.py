from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    emailConfirmed = models.BooleanField(default=False)
    gender = models.CharField(max_length=2,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    phoneConfirmed = models.BooleanField(default=False)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    area = models.CharField(max_length=20,null=True,blank=True)

class axisAwards(models.Model):
    awardName = models.CharField(max_length=20,unique=True)
    awardType = models.IntegerField(default=0)
    # 0 = OnceInALifeTime , 1 = Incremental,
    awardDesc = models.CharField(max_length=100,null=True)

class userAwards(models.Model):
    awardId = models.ForeignKey(axisAwards,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "%s \t %s \t %d" % (self.awardId,self.user, self.count)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Awards.objects.create(awardId=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.awards.save()
'''