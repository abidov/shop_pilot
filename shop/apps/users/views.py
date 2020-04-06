from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UserSerializer, BookmarkSerializer
from .models import Bookmark


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer