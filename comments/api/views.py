from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from comments.models import Comment
from users.models import User
from meetings.models import Meeting

from comments.api.serializers import CommentsSerializer

class CommentsListView(ListAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

class CommentsDetailView(RetrieveAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

class CommentsDeleteView(DestroyAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

class CommentsCreateView(CreateAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

    def post(self, request, *args, **kwargs):

        comment = Comment()

        meeting = Meeting.objects.get(id = request.data.get('meeting'))
        user = User.objects.get(id = request.data.get('user'))

        comment.description = request.data.get('description')
        comment.meeting = meeting
        comment.user = user

        comment.save()
        serializer = CommentsSerializer(instance = comment, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class CommentsUpdateView(UpdateAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

    def put(self, request, *args, **kwargs):

        comment = Comment.objects.get(id = request.data.get('commentID'))
        meeting = Meeting.objects.get(id = request.data.get('meetingID'))
        user = User.objects.get(id = request.data.get('userID'))
        comment.description = request.data.get('description')
        comment.meeting = meeting
        comment.user = user

        comment.save()
        serializer = CommentsSerializer(instance = comment, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)