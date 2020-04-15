from django.urls import path
from images.api.views import ImageListView, ImageDetailView, ImageCreateView

urlpatterns = [
    path('', ImageListView.as_view()),
    path('create/', ImageCreateView.as_view()),
    path('detail/<int:pk>/', ImageDetailView.as_view()),
]