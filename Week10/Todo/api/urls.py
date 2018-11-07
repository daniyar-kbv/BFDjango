from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.lists_list),
    path('list/<int:pk>/', views.list_detail),
    path('task/', views.task_list),
    path('task/<int:pk>/', views.task_detail),
]