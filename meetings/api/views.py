from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify

from users.models import User
from meetings.models import Meeting
from projects.models import Project
from rules.models import Rules
from agenda.models import Agenda
from questionnaires.models import Questionnaire
from questions.models import Questions
from choices.models import Choice

from meetings.api.serializers import MeetingSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingDetailView(RetrieveAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()
    lookup_field = 'slug'

class MeetingDeleteView(DestroyAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingCreateView(CreateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def post(self, request, *args, **kwargs):

        meeting = Meeting()

        project = Project.objects.get(id = request.data.get('project'))
        meeting_leader = User.objects.get(id = request.data.get('meeting_leader'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.project = project
        meeting.meeting_leader = meeting_leader
        meeting.duration_time = None
        meeting.real_hour = None
        meeting.real_date = None
        meeting.questtionaire = None

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class MeetingUpdateView(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        project = Project.objects.get(id = request.data.get('projectID'))
        meeting_leader = User.objects.get(id = request.data.get('userID'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.project = project
        meeting.meeting_leader = meeting_leader
        meeting.duration_time = None
        meeting.real_hour = None
        meeting.real_date = None

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class MeetingsListView(ListAPIView):

    serializer_class = MeetingSerialize

    def get_queryset(self):
        project_slug = self.kwargs['slug']
        project = Project.objects.get(slug = project_slug)
        queryset = Meeting.objects.filter(project = project)

        return queryset

class MeetingAddUsers(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        project = Project.objects.get(id = request.data.get('projectID'))
        meeting_leader = User.objects.get(id = request.data.get('userID'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.project = project
        meeting.meeting_leader = meeting_leader
        meeting.duration_time = None
        meeting.real_hour = None
        meeting.real_date = None

        for users in request.data.get('users'):
            new_user = User.objects.get(id = users['id'])
            meeting.users.add(new_user)

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class MeetingRemoveUsers(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        project = Project.objects.get(id = request.data.get('projectID'))
        meeting_leader = User.objects.get(id = request.data.get('userID'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.project = project
        meeting.meeting_leader = meeting_leader
        meeting.duration_time = None
        meeting.real_hour = None
        meeting.real_date = None

        for users in request.data.get('users'):
            delete_user = User.objects.get(id = users['id'])
            meeting.users.remove(delete_user)

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class MeetingAddItems(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        project = Project.objects.get(id = request.data.get('projectID'))
        meeting_leader = User.objects.get(id = request.data.get('userID'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.project = project
        meeting.meeting_leader = meeting_leader
        meeting.duration_time = None
        meeting.real_hour = None
        meeting.real_date = None

        rules_request = request.data.get('rules')
        agendas_request = request.data.get('agendas')

        list_rules_in_meeting = meeting.rules.all()
        list_rules_request = []
        list_rules = []
        list_agendas_in_meeting = meeting.agendas.all()
        list_agendas_request = []
        list_agendas = []

        for rules in rules_request:
            list_rules_request.append(rules['title'])

        for rules in list_rules_in_meeting:
            list_rules.append(rules.title)

        for agendas in agendas_request:
            list_agendas_request.append(agendas['title'])

        for agendas in list_agendas_in_meeting:
            list_agendas.append(agendas.title)

        final_list_rules = [ item for item in list_rules_request if item not in list_rules ]
        final_list_agenda = [ item for item in list_agendas_request if item not in list_agendas ]

        for rules in final_list_rules:

            new_rule = Rules()
            new_rule.title = rules
            new_rule.save()
            meeting.rules.add(new_rule)

        for agendas in final_list_agenda:

            new_agenda = Agenda()
            new_agenda.title = agendas
            new_agenda.save()
            meeting.agendas.add(new_agenda)

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class FinishMeeting(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        project = Project.objects.get(id = request.data.get('projectID'))
        meeting_leader = User.objects.get(id = request.data.get('userID'))

        meeting.title = request.data.get('title')
        meeting.status = request.data.get('status')
        meeting.slug = slugify(meeting.title)
        meeting.initial_date = request.data.get('initial_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.duration_time = request.data.get('duration_time')
        meeting.real_hour = request.data.get('real_hour')
        meeting.real_date = request.data.get('real_date')
        meeting.project = project
        meeting.meeting_leader = meeting_leader

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class AddQuesttionaire(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):

        meeting = Meeting.objects.get(slug = request.data.get('slug'))

        questtionaire = Questionnaire()
        questtionaire.title = request.data.get('questtionaire')['title']
        questtionaire.save()
        meeting.questtionaire = questtionaire
        order = 1

        for question in request.data.get('questtionaire')['questions']:

            new_question = Questions()
            new_question.title = question['title']
            new_question.order = order
            new_question.save()

            for user in meeting.users.all():

                if user.name == str(meeting.meeting_leader):
                    print('Usuário é o Lider da Reunião')
                else:
                    new_question.users.add(user)

            for choice in question.get('choices'):
                new_choice = Choice()
                new_choice.title = choice
                new_choice.save()
                new_question.choices.add(new_choice)

            new_question.questtionaire = questtionaire
            new_question.save()
            order += 1

        meeting.save()
        serializer = MeetingSerialize(instance = meeting, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)