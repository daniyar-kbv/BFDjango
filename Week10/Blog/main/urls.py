from django.urls import path
from main import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, CreateCommentView, PostDeleteView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('<int:fk>/post', PostDetailView.as_view()),
    path('create_fk', PostCreateView.as_view()),
    path('<int:fk>/create_comment', CreateCommentView.as_view()),
    path('<int:fk>/delete_post', PostDeleteView.as_view()),
    path('<int:fk>/update_post', PostUpdateView.as_view()),
    path('<int:fk>/delete_comment/<int:comment>', CommentDeleteView.as_view()),
    path('<int:fk>/update_comment/<int:comment>', CommentUpdateView.as_view()),
]