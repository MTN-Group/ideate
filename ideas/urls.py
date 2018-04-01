from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ideas', views.IdeaViewsSet)

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
