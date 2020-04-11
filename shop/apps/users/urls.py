
from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
<<<<<<< HEAD
    path('create/', views.UserCreateView.as_view(), name='user-create'),
=======
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/bookmark/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
]