from rest_framework import generics
from django.contrib.auth.models import User

<<<<<<< HEAD
from .serializers import UserSerializer, BookmarkSerializer, UserCreateSerializer
=======
from .serializers import UserSerializer, BookmarkSerializer
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
from .models import Bookmark


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


<<<<<<< HEAD
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


=======
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer