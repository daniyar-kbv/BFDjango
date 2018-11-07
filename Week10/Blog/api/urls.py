from django.urls import path
from api2 import views

urlpatterns = [
    path('posts/', views.students_list),
    path('posts/<int:pk>/', views.students_detail),
    path('comments/', views.comments_list),
    path('comments/<int:pk>/', views.comments_detail),
]
