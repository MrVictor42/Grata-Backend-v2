from django.urls import path

from choices.api.views import ChoiceListView

urlpatterns = [
    path('', ChoiceListView.as_view()),
]