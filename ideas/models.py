from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()

class Category ( models.Model ):
    name = models.CharField( max_length=100 )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Challenge(Post):
    categories = models.ManyToManyField(Category)

class Idea(Post):
    votes = models.IntegerField(default=0)
    tags = TaggableManager()
    version = models.IntegerField(default=0)
    challenges = models.ManyToManyField(Challenge, blank=True)
    linked_ideas = models.ManyToManyField('self', blank=True, related_name='ideas')

class Comments(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
