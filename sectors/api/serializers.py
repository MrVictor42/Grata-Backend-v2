from rest_framework.serializers import ModelSerializer
from sectors.models import Sector

class SectorSerialize(ModelSerializer):

    class Meta:

        model = Sector
        fields = ('__all__')
        lookup_field = 'slug'