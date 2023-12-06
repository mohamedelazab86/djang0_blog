from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):

    title=models.CharField(max_length=100,verbose_name=_('name'))
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    content=models.TextField(max_length=1000)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    now=models.DateTimeField(auto_now=True)
    iamge=models.ImageField(upload_to='image/%y-%m-%d')
    slug=models.SlugField(null=True,blank=True)
    tags = TaggableManager()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

    
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comment(models.Model):
    author=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    publish_date=models.DateTimeField(auto_now=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')

    def __str__(self):
        return str(self.post)
    
class ImagePost(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='imagepost_post')
    iamge=models.ImageField(upload_to='image/%y-%m-%d')

    def __str__(self):
        return f'{self.post}'
    




