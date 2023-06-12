from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path


from accounts.views import UserProfileAPIView, AuthorizedUsersView
from chat_room.views import Rooms, Dialog

urlpatterns = [

    path("profile/", UserProfileAPIView.as_view()),
    path('authorized-users/', AuthorizedUsersView.as_view(), name='authorized_users'),
    path('login/', LoginView.as_view(), name='login'),
]