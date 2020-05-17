from django.urls import path

from meetings.api.views import MeetingListView, MeetingCreateView, \
                               MeetingDeleteView, MeetingDetailView, MeetingUpdateView, \
                               MeetingsListView

urlpatterns = [
    path('', MeetingListView.as_view()),
    path('create/', MeetingCreateView.as_view()),
    path('detail/<pk>/', MeetingDetailView.as_view()),
    path('update/<pk>/', MeetingUpdateView.as_view()),
    path('delete/<pk>/', MeetingDeleteView.as_view()),
    path('meetings_in_project/<pk>/', MeetingsListView.as_view())
]