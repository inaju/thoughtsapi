from django.urls import path
from rest_framework.routers import DefaultRouter
from.views import UserProfileListCreateView, UserProfileDetailView, list_location
from . import get_user

urlpatterns = [
    path('all-profiles', UserProfileListCreateView.as_view(), name='all-profiles'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(),name='profile'),
    path('profile/<int:pk>/location/', list_location, name='location'),
    path('get-user/', get_user.ExampleView.as_view())
]
