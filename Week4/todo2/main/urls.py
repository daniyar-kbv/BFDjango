from django.urls import path

from main import views

urlpatterns = [
    path('', views.show_lists),
    path('<int:list>/todo', views.todo_list),
    path('<int:list>/completed', views.completed_todo_list),
]