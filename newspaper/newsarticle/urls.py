from django.urls import path
from .views import (
    PostPreview, NewsPreview, PostCreate,
    PostEdit, PostDelete, ArticleCreate,
)

urlpatterns = [
    path('', PostPreview.as_view(), name='posts_list'),
    path('news/', PostPreview.as_view(), name='posts_list'),
    path('articles/', PostPreview.as_view(), name='posts_list'),
    path('news/<int:pk>/', NewsPreview.as_view(), name='post_preview'),
    path('articles/<int:pk>/', NewsPreview.as_view(), name='post_preview'),
    path('news/create/', PostCreate.as_view(), name='create_post'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='edit_post'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    path('articles/create/', ArticleCreate.as_view(), name='create_article'),
    path('articles/<int:pk>/edit/', PostEdit.as_view(), name='edit_article'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='delete_article'),
]
