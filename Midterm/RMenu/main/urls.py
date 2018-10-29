from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.show_rests),
    path('<int:fk>/dishes', views.show_dishes),
    path('create_rest', views.create_rest)
]