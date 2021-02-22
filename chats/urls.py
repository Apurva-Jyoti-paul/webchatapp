from . import views
from django.urls import path


urlpatterns=[
    path('send/',views.send,name='send'),
    path('home/',views.mainv,name='mainv'),
    path('create/',views.create,name='create'),
]