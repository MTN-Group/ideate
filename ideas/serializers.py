from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ideas.models import Idea, Category, Category, Tag, Comments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ('title', 'post_text', 'submitter')
