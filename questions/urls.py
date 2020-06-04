from django.urls import path

from questions.api.views import QuizListView, QuizDetailView, QuizDelete

urlpatterns = [

    path('', QuizListView.as_view()),
    path('detail/<pk>/', QuizDetailView.as_view()),
    path('delete/<pk>/', QuizDelete.as_view())
]