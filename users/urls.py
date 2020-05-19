from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete, UserInSector, \
                            UsersProjectInListView, UsersProjectNotInListView, \
                            UsersInProjectAndMeetingListView, UsersInProjectAndNotMeetingListView

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('user_detail/<pk>/', UserDetail.as_view()),
    path('user_edit/<pk>/', UserUpdate.as_view()),
    path('user_delete/<pk>/', UserDelete.as_view()),
    path('users_in_sector/<pk>/', UserInSector.as_view()),
    path('users_in_project/<pk>/', UsersProjectInListView.as_view()),
    path('users_not_in_project/<pk>/', UsersProjectNotInListView.as_view()),
    path('users_in_project_and_meeting/<pk_meeting>/<pk_project>/', UsersInProjectAndMeetingListView.as_view()),
    path('users_in_project_and_not_in_meeting/<pk_meeting>/<pk_project>', UsersInProjectAndNotMeetingListView.as_view()),
]