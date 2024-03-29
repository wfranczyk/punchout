from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag, Category, Task, TaskTag, Board
from .serializers import BoardSerializer, CategorySerializer

class GetBoardsView(APIView):
    def get(self, request, *args, **kwargs):
        data = BoardSerializer(Board.objects.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)

class CategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
