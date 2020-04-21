from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lite, name='post_list'),
]