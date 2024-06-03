from django.urls import path
from .views import index,contact,create,mark

urlpatterns = [
    path('',index),
    path('contact',contact),
    path('create',create),
    path('mark/<pk>',mark)
]