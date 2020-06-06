from django.urls import path

from gradedQuesttionaire.api.views import GradedQuesttionaireListView, GradedQuesttionaireCreate

urlpatterns = [
    path('', GradedQuesttionaireListView.as_view()),
    path('create/', GradedQuesttionaireCreate.as_view())
]