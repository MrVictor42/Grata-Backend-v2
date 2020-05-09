from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete, UserInSector, \
                            UsersProjectInListView

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('user_detail/<pk>/', UserDetail.as_view()),
    path('user_edit/<pk>/', UserUpdate.as_view()),
    path('user_delete/<pk>/', UserDelete.as_view()),
    path('users_in_sector/<pk>/', UserInSector.as_view()),
    path('users_in_project/<pk>/', UsersProjectInListView.as_view()),
]