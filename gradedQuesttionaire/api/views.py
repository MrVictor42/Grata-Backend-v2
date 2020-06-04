from rest_framework.generics import ListAPIView, CreateAPIView

from gradedQuesttionaire.api.serializers import GradedQuesttionaireSerialize
from gradedQuesttionaire.models import GradedQuesttionaire

class GradedQuesttionaireListView(ListAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

class GradedQuesttionaireCreate(CreateAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

    def post(self, request, *args, **kwargs):

        gradedQuesttionaire = GradedQuesttionaire()