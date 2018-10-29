from django.urls import path, include
from main.views import HomeView, CreateRestView, DishesView, CreateDishView, DeleteRestView, UpdateRestView
from main import views


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:fk>/dishes', DishesView.as_view()),
    path('create_rest', CreateRestView.as_view()),
    path('<int:fk>/create_dish', CreateDishView.as_view()),
    path('<int:fk>/delete_rest', DeleteRestView.as_view()),
    path('<int:fk>/update_rest', UpdateRestView.as_view()),
]