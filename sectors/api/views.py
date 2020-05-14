from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
                                    DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify

from sectors.models import Sector
from sectors.api.serializers import SectorSerialize

class SectorCreateView(CreateAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

    def post(self, request, *args, **kwargs):

        sector = Sector()

        sector.initials = request.data.get('initials')
        sector.name = request.data.get('name')
        sector.slug = slugify(sector.name)

        sector.save()
        serializer = SectorSerialize(instance = sector, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class SectorUpdateView(UpdateAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

    def put(self, request, *args, **kwargs):

        sector = Sector.objects.get(id = request.data.get('sectorID'))

        sector.initials = request.data.get('initials')
        sector.name = request.data.get('name')
        sector.slug = slugify(sector.name)

        sector.save()
        serializer = SectorSerialize(instance = sector, data = request.data)
        serializer.is_valid(raise_exception = True)

        return Response(serializer.data)

class SectorListView(ListAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

class SectorDetailView(RetrieveAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()
    lookup_field = 'slug'

class SectorDeleteView(DestroyAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()