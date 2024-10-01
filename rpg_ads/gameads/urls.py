from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('', views.ad_list, name='ad_list'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('ad/create/', views.ad_create, name='ad_create'),
    path('ad/<int:pk>/edit/', views.ad_edit, name='ad_edit'),
    path('my-replies/', views.user_replies, name='user_replies'),
    path('profile/', profile, name='profile'),

    # Добавляем маршрут для выхода
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL для выхода
]
