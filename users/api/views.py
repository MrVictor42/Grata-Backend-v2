from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.api.serializers import UserSerializer

class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdate(UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):

        user = self.get_object()
        user.username = request.data.get('username')
        user.email = request.data.get('email')
        user.name = request.data.get('name')
        user.ramal = request.data.get('ramal')

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
        serializer = UserSerializer(
            instance = user,
            data = request.data
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class UserDelete(DestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()