from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('user_detail/<int:pk>/', UserDetail.as_view()),
    path('user_edit/<int:pk>/', UserUpdate.as_view()),
    path('user_delete/<int:pk>/', UserDelete.as_view())
]