from django.urls import path
from .views import register
from . import views

urlpatterns = [

    path('register/', register, name='register'),

    path('', views.ad_list, name='ad_list'),

    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),

    path('ad/create/', views.ad_create, name='ad_create'),

    path('ad/<int:pk>/edit/', views.ad_edit, name='ad_edit'),

    path('my-replies/', views.user_replies, name='user_replies'),
]
