from rest_framework.serializers import ModelSerializer

from comments.models import Comment
from users.api.serializers import StringSerializer

class CommentsSerializer(ModelSerializer):

    user = StringSerializer(many = False)

    class Meta:

        model = Comment
        fields = ('__all__')