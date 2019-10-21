from django.urls import path
from . import views

urlspatterns = [
    path('', view.port_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name= 'post_detail'),
]