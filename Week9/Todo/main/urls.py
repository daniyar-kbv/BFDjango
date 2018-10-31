from django.urls import path
from main import views
from main.views import ListsView, TodoListView, CompTodoListView, CreateListView, MakeDoneView, MakeNotDoneView, DeleteListView

urlpatterns = [
    path('', ListsView.as_view(), name='home'),
    path('<int:list>/todo', TodoListView.as_view()),
    path('<int:list>/completed', CompTodoListView.as_view()),
    path('create_list', CreateListView.as_view()),
    path('<int:fk>/delete_list', DeleteListView.as_view()),
    path('<int:fk>/task_done/<int:pk>', MakeDoneView.as_view()),
    path('<int:fk>/task_notdone/<int:pk>', MakeNotDoneView.as_view()),
]