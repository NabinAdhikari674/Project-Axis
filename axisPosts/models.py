from django.db import models
#from django.utils.text import slugify
from axisUsers.models import User
from autoslug import AutoSlugField
#import re

# Create your models here.
class Post(models.Model):
    postTitle = models.CharField(max_length=200,unique=False)
    postSlug = AutoSlugField(populate_from="postTitle",unique=True)
    postAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="1")
    statusChoices = [('0', 'Draft/Not Published'),('1', 'Published')]
    status = models.IntegerField(default=0) #Draft or Published
    content = models.TextField()
    postimage = models.ImageField(upload_to="images")
    category = models.IntegerField(default=0) #Post Category:Regular/Complaint/Concern/Movement/Awareness
    axisStatus = models.IntegerField(default=0) # Issue Status : Planning/OnGoing/Ended/Cancelled/Suspended
    postLevel = models.IntegerField(default=0) #Post Type/Level : Gov/Community/Private/Charity/Org
    budget = models.IntegerField(null=True,blank=True,default=0)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    popularity = models.BigIntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-popularity']
    def __str__(self):
        return self.postTitle

class postComments(models.Model):
    postId =  models.ForeignKey(Post,on_delete= models.CASCADE)
    active = models.BooleanField(default=True)
    parentId = models.ForeignKey('self',related_name='replies',on_delete= models.SET_NULL,null=True, blank=True)
    commentAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="1")
    comment = models.TextField()
    popularity = models.IntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-popularity']

class postReactions(models.Model):
    postId = models.ForeignKey(Post,on_delete= models.CASCADE)
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()

class commentReactions(models.Model):
    commentId = models.ForeignKey(postComments,on_delete=models.CASCADE)
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()

'''
def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value
'''