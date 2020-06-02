from django.urls import path

from quiz.api.views import QuizListView, QuizDetailView

urlpatterns = [

    path('', QuizListView.as_view()),
    path('detail/<pk>/', QuizDetailView.as_view())
]