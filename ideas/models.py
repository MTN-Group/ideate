from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=False)

class Category ( models.Model ):
    name = models.CharField( max_length=100 )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=30)
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.post_text

class Challenge(Post):
    categories = models.ManyToManyField(Category)

class Idea(Post):
    votes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag,related_name='ideas')
    version = models.IntegerField(default=0)
    challenges = models.ManyToManyField(Challenge)
    
class Comments(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
