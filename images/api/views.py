from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

from images.models import Image
from images.api.serializers import ImageSerializer

class ImageListView(ListAPIView):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ImageDetailView(RetrieveAPIView):

    serializer_class = ImageSerializer
    queryset =  Image.objects.all()

class ImageCreateView(CreateAPIView):

    serializer_class = ImageSerializer

    def post(self, request):

        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)