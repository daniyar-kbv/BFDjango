from django.urls import path
from main import views

urlpatterns = [
    path('', views.show_posts),
    path('<int:post>/post', views.post_more),
]