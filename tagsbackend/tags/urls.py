# importing django routing libraries
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_feed, name='home_feed'),
    path('add/', add_post, name='add_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit_tags/', edit_tags, name='edit_tags'),
]