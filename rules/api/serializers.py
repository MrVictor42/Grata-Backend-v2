from rest_framework.serializers import ModelSerializer

from rules.models import Rules

class RulesSerialize(ModelSerializer):

    class Meta:

        model = Rules
        fields = ('__all__')