from django.db import models
from axisUsers.models import User

# Create your models here.
class monitorPost(models.Model):
    projectTitle = models.CharField(max_length=200,unique=False)
    projectSlug = models.SlugField(max_length=200,unique=True)
    projectAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="AnynomousAxisUser")
    projectBudget=models.IntegerField(default=0)
    projectDeadline=models.DateTimeField(auto_now=True)
    projectArea=models.CharField(max_length=200,unique=False)
    #statusChoices = [('0', 'Draft/Not Published'),('1', 'Published')]
    status = models.IntegerField(default=0)
    content = models.TextField()
    category = models.IntegerField(default=0)
    axisStatus = models.IntegerField(default=0)
    popularity = models.BigIntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['popularity']
    def __str__(self):
        return self.projectTitle

class monitirComments(models.Model):
    projectId = models.BigIntegerField()
    parentId = models.IntegerField()
    commentAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="AnynomousAxisUser")
    comment = models.TextField()
    popularity = models.IntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    #class Meta:
    #    ordering = ['popularity']
    #def __str__(self):
    #    return self.userName

class monitorPostReactions(models.Model):
    projectId = models.BigIntegerField()
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()

class monitorCommentReactions(models.Model):
    commentId = models.IntegerField()
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()
