from django.urls import path

from choices.api.views import ChoiceListView, ChoicesQuestion

urlpatterns = [
    path('', ChoiceListView.as_view()),
    path('list_choices/<pk>/', ChoicesQuestion.as_view())
]