from django.urls import path

from comments.api.views import CommentsListView, CommentsCreateView, CommentMeeting

urlpatterns = [
    path('', CommentsListView.as_view()),
    path('create/', CommentsCreateView.as_view()),
    path('list_comments_in_meeting/<pk>/', CommentMeeting.as_view())
]