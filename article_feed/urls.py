from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='main'),
    path('article/<slug:article_slug>', post, name='article'),
    path('categories/<str:name>', postCategory, name='category'),
    
]