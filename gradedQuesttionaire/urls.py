from django.urls import path

from gradedQuesttionaire.api.views import GradedQuesttionaireListView, GradedQuesttionaireCreate, \
                                          GradedInQuesttionaire, UserInGraded

urlpatterns = [
    path('', GradedQuesttionaireListView.as_view()),
    path('create/', GradedQuesttionaireCreate.as_view()),
    path('graded_questtionaire/<pk>/', GradedInQuesttionaire.as_view()),
    path('user_in_graded/<pk>/', UserInGraded.as_view())
]