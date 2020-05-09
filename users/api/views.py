from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from users.models import User
from images.models import Image
from sectors.models import Sector
from projects.models import Project

from projects.api.serializers import ProjectSerialize
from users.api.serializers import UserSerializer, UserSerializerUpdate

class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdate(UpdateAPIView):

    serializer_class = UserSerializerUpdate
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):

        user = User.objects.get(id = request.data.get('id'))
        sector = request.data.get('sector')
        image = request.data.get('image')

        user.username = request.data.get('username')
        user.email = request.data.get('email')
        user.name = request.data.get('name')
        user.ramal = request.data.get('ramal')
        user.description = request.data.get('description')

        if sector == None or sector == '' or sector is None:
            user.sector = None
        else:
            sector = Sector.objects.get(id = request.data.get('sector'))
            user.sector = sector

        if image == None or image == '' or image is None:
            pass
        else:
            image = Image.objects.get(id = request.data.get('image'))
            user.image = image

        if request.data.get('is_administrator') is None:
            user.is_administrator = False
        else:
            user.is_administrator = True
        if request.data.get('is_participant') is None:
            user.is_participant = False
        else:
            user.is_participant = True

        if user.is_administrator == True:

            user.is_participant = False
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True

        else:

            user.is_participant = True
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True

        user.save()
        serializer = UserSerializer(instance = user, data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response(serializer.data)

class UserDelete(DestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserInSector(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        sector_id = self.kwargs['pk']
        queryset = User.objects.filter(sector = sector_id)

        return queryset

class UsersProjectInListView(ListAPIView):

    serializer_class = ProjectSerialize

    def get_queryset(self):

        project_id = self.kwargs['pk']
        current_project = Project.objects.get(id = project_id)
        users_project = current_project.users.all()

        return users_project