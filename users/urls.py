from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('show_user/<int:pk>/', UserDetail.as_view()),
    path('update_user/<int:pk>/', UserUpdate.as_view()),
    path('delete_user/<int:pk>/', UserDelete.as_view())
]