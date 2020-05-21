from django.urls import path

from rules.api.views import RulesListView, RulesMeeting

urlpatterns = [
    path('', RulesListView.as_view()),
    path('rules_in_meeting/<pk>/', RulesMeeting.as_view())
]