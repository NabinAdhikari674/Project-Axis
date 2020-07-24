from django.db import models

# Create your models here.
class axisUser(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField()
