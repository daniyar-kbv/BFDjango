from django.urls import path
from api import views

urlpatterns = [
    path('posts/', views.posts_list),
    path('posts/<int:pk>/', views.posts_detail),
    path('comments/', views.comments_list),
    path('comments/<int:pk>/', views.comments_detail),
]
