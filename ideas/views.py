#from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . import serializers
from ideas.models import Idea, Category, Category, Comments


def index(request):
    return HttpResponse("Hello, world. You're at the ideas index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

class IdeaViewsSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all().order_by('pub_date')
    serializer_class = serializers.IdeaSerializer
