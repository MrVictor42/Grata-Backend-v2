from django.urls import path

from meetings.api.views import MeetingListView, MeetingCreateView, \
                               MeetingDeleteView, MeetingDetailView, MeetingUpdateView, \
                               MeetingsListView, MeetingAddUsers, MeetingRemoveUsers, \
                               MeetingAddItems, FinishMeeting

urlpatterns = [
    path('', MeetingListView.as_view()),
    path('create/', MeetingCreateView.as_view()),
    path('detail/<pk>/', MeetingDetailView.as_view()),
    path('update/<pk>/', MeetingUpdateView.as_view()),
    path('delete/<pk>/', MeetingDeleteView.as_view()),
    path('meetings_in_project/<slug>/', MeetingsListView.as_view()),
    path('add_users_meeting/<pk>/', MeetingAddUsers.as_view()),
    path('remove_users_meeting/<pk>/', MeetingRemoveUsers.as_view()),
    path('add_items/<pk>/', MeetingAddItems.as_view()),
    path('finish_meeting/<pk>/', FinishMeeting.as_view())
]