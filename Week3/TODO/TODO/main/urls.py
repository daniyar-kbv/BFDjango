from django.urls import path

from main import views

urlpatterns = [
    path('', views.todo_list),
    path('completed', views.completed_todo_list),
]