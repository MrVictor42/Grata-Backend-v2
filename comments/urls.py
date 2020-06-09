from django.urls import path

from comments.api.views import CommentsListView, CommentsCreateView, CommentQuesttionaire

urlpatterns = [
    path('', CommentsListView.as_view()),
    path('create/', CommentsCreateView.as_view()),
    path('list_comments_in_questtionaire/<pk>/', CommentQuesttionaire.as_view())
]