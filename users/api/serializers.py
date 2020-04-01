from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User

class StringSerializer(serializers.StringRelatedField):

    def to_internal_value(self, value):

        return value

class UserSerializer(serializers.ModelSerializer):

    sector = StringSerializer(many = False)

    class Meta:

        model = User
        fields = ('id', 'email', 'username', 'ramal',
                  'name', 'sector', 'is_administrator', 'is_participant')

class CustomRegisterSerializer(RegisterSerializer):

    is_participant = serializers.BooleanField(default = False)
    is_administrator = serializers.BooleanField(default = False)
    ramal = serializers.CharField(max_length = 6)
    name = serializers.CharField(max_length = 40)

    class Meta:

        model = User
        fields = ('email', 'username', 'ramal', 'name', 'password', 'is_administrator', 'is_participant')

    def get_cleaned_data(self):

        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'ramal': self.validated_data.get('ramal', ''),
            'name': self.validated_data.get('name', ''),
            'is_administrator': self.validated_data.get('is_administrator', ''),
            'is_participant': self.validated_data.get('is_participant', '')
        }

    def save(self, request):

        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.is_participant = self.cleaned_data.get('is_participant')
        user.is_administrator = self.cleaned_data.get('is_administrator')
        user.name = self.cleaned_data.get('name')
        user.ramal = self.cleaned_data.get('ramal')

        if user.is_administrator == True:

            user.is_staff = True
            user.is_superuser = True
            user.is_active = True

        else :

            user.is_staff = False
            user.is_superuser = False
            user.is_active = True

        user.save()
        adapter.save_user(request, user, self)

        return user

class TokenSerializer(serializers.ModelSerializer):

    user_type = serializers.SerializerMethodField()

    class Meta:

        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):

        serializer_data = UserSerializer(
            obj.user
        ).data
        is_administrator = serializer_data.get('is_administrator')
        is_participant = serializer_data.get('is_participant')
        return {
            'is_participant': is_participant,
            'is_administrator': is_administrator
        }