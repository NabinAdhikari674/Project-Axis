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
    membershipDate = models.DateField(auto_now_add=True)


class Awards(models.Model):
    awardId = models.OneToOneField(User, on_delete=models.CASCADE)
    award = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "%s \t %s \t %d" % (self.awardId, self.award, self.count)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Awards.objects.create(awardId=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.awards.save()
