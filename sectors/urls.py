from django.urls import path

from sectors.api.views import SectorListView, SectorCreateView, SectorDetailView, \
                              SectorUpdateView, SectorDeleteView

urlpatterns = [
    path('', SectorListView.as_view()),
    path('create/', SectorCreateView.as_view()),
    path('detail/<int:pk>/', SectorDetailView.as_view()),
    path('update/<int:pk>/', SectorUpdateView.as_view()),
    path('delete/<int:pk>/', SectorDeleteView.as_view())
]