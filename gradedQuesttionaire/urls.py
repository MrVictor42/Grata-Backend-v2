from django.urls import path

from gradedQuesttionaire.api.views import GradedQuesttionaireListView

urlpatterns = [
    path('', GradedQuesttionaireListView.as_view())
]