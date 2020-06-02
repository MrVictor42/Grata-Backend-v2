from rest_framework.generics import ListAPIView
from choices.models import Choice
from choices.api.serializers import ChoiceSerialize

class ChoiceListView(ListAPIView):

    serializer_class = ChoiceSerialize
    queryset = Choice.objects.all()