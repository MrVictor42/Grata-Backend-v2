from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('user_detail/<pk>/', UserDetail.as_view()),
    path('user_edit/<pk>/', UserUpdate.as_view()),
    path('user_delete/<pk>/', UserDelete.as_view())
]