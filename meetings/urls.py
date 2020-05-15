from django.urls import path

from meetings.api.views import MeetingListView, MeetingCreateView, \
                               MeetingDeleteView, MeetingDetailView, MeetingUpdateView

urlpatterns = [
    path('', MeetingListView.as_view()),
    path('create/', MeetingCreateView.as_view()),
    path('detail/<pk>/', MeetingDetailView.as_view()),
    path('update/<pk>/', MeetingUpdateView.as_view()),
    path('delete/<pk>/', MeetingDeleteView.as_view()),
]