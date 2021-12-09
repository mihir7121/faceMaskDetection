from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path("rendervideo", views.rendervideo, name='rendervideo'),
]