from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import PageSerializer, PageTypeSerializer

class PageTypeListCreateView(APIView):
    def get(self, request):
        page_types = PageTypeModel.objects.all()
        serializer = PageTypeSerializer(page_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PageListCreateView(APIView):
    def get(self, request):
        pages = PageContentModel.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
