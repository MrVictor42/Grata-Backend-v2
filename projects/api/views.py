from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify

from projects.models import Project
from sectors.models import Sector
from users.models import User

from projects.api.serializers import ProjectSerialize

class ProjectListView(ListAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectDetailView(RetrieveAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()
    lookup_field = 'slug'

class ProjectDeleteView(DestroyAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectCreateView(CreateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

    def post(self, request, *args, **kwargs):

        project = Project()

        project.title = request.data.get('title')
        project.status = request.data.get('status')
        project.slug = slugify(project.title)
        sector = request.data.get('sector')

        if sector == None or sector == '':
            sector = None
        else:
            sector = Sector.objects.get(id = request.data.get('sector'))

        project.sector = sector

        project.save()
        serializer = ProjectSerialize(instance = project, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class ProjectUpdateView(UpdateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

    def put(self, request, *args, **kwargs):

        project = Project.objects.get(id = request.data.get('projectID'))
        sector = Sector.objects.get(id = request.data.get('sector'))

        project.title = request.data.get('title')
        project.status = request.data.get('status')
        project.slug = slugify(project.title)
        project.sector = sector

        project.save()
        serializer = ProjectSerialize(instance = project, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class ProjectsListView(ListAPIView):

    serializer_class = ProjectSerialize

    def get_queryset(self):
        sector_id = self.kwargs['pk']
        queryset = Project.objects.filter(sector = sector_id)

        return queryset

class ProjectAddUsers(UpdateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

    def put(self, request, *args, **kwargs):

        project = Project.objects.get(id = request.data.get('projectID'))
        sector = Sector.objects.get(id = request.data.get('sector'))

        project.title = request.data.get('title')
        project.status = request.data.get('status')
        project.slug = slugify(project.title)
        project.sector = sector

        for users in request.data.get('users'):

            new_user = User.objects.get(id = users['id'])
            project.users.add(new_user)

        project.save()
        serializer = ProjectSerialize(instance = project, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class ProjectRemoveUsers(UpdateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

    def put(self, request, *args, **kwargs):

        project = Project.objects.get(id = request.data.get('projectID'))
        sector = Sector.objects.get(id = request.data.get('sector'))

        project.title = request.data.get('title')
        project.status = request.data.get('status')
        project.slug = slugify(project.title)
        project.sector = sector

        for users in request.data.get('users'):

            delete_user = User.objects.get(id = users['id'])
            project.users.remove(delete_user)

        project.save()
        serializer = ProjectSerialize(instance = project, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)