from django.contrib import admin
from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView,LogoutAPIView, ToDoAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('home/', UserAPIView.as_view()),
    path('refresh/', RefreshAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('todo/', ToDoAPIView.as_view()),

]