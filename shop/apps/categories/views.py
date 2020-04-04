from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer, CategoryCreateSerializer
from rest_framework.response import Response
from rest_framework import status



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = CategoryCreateSerializer(queryset)
        
        