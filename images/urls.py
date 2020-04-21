from django.urls import path
from images.api.views import ImageListView, ImageDetailView, ImageCreateView, \
                             ImageDestroyView, ImageUpdateView

urlpatterns = [
    path('', ImageListView.as_view()),
    path('create/', ImageCreateView.as_view()),
    path('detail/<int:pk>/', ImageDetailView.as_view()),
    path('update/<int:pk>/', ImageUpdateView.as_view()),
    path('delete/<int:pk>/', ImageDestroyView.as_view())
]