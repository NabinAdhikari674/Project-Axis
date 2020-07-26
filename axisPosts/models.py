from django.db import models
from axisUsers.models import User

# Create your models here.
class Post(models.model):
    postId = modes.AutoField()
    postTitle = models.CharField(max_length=200)
    postSlug = models.SlugField(max_length=200,unique=True)
    postAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="AnynomousAxisUser")
    statusChoices = [('0', 'Draft/Not Published'),('1', 'Published')]
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()
    popularity = models.BigIntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['popularity']
    def __str__(self):
        return self.postTitle

class postComments(models.model):
    commentId = models.AutoField()

class postReactions(models.model):
    reactionId = models.AutoField()
