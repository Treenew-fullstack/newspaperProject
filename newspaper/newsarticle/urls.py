from django.urls import path
from .views import PostPreview, NewsPreview


urlpatterns = [
    path('', PostPreview.as_view()),
    path('<int:pk>', NewsPreview.as_view()),
]