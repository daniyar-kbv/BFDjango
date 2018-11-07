from django.urls import path
from api1 import views


urlpatterns = [
    path('index/', views.index),
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail),
]
