from django.urls import path
from main import views

urlpatterns = [
    path('', views.show_posts),
    path('<int:post>/post', views.post_more),
    path('create_post', views.create_post),
    path('<int:post>/create_comment', views.create_comment),
    path('<int:post>/delete_post', views.delete_post),
    path('<int:post>/update_post', views.update_post),
    path('<int:post>/delete_comment/<int:comment>', views.delete_comment),
    path('<int:post>/update_comment/<int:comment>', views.update_comment),
]