from django.urls import path
from api2 import views

urlpatterns = [
    path('students/', views.students_list),
    path('students/<int:pk>/', views.students_detail)
]
