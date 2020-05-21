from django.urls import path

from agenda.api.views import AgendaListView, AgendasMeeting

urlpatterns = [
    path('', AgendaListView.as_view()),
    path('agendas_in_meeting/<pk>/', AgendasMeeting.as_view())
]