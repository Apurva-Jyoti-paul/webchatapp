from . import views
from django.urls import path


urlpatterns=[
    path('send/',views.send,name='send'),
    path('home/',views.mainv,name='mainv'),
    path('create/',views.create,name='create'),
    path('<key>/see/',views.see,name='see'),
    path('<key>/adduser/',views.adduser,name='adduser'),
    path('<key>/<c>/add/',views.add,name='add'),
]