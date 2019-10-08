from django.urls import path
from . import views

urlspatterns = [
    path('', view.port_list, name = 'post_list'),
]