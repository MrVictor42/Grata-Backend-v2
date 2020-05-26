from django.urls import path

from comments.api.views import CommentsListView

urlpatterns = [
    path('', CommentsListView.as_view()),
]