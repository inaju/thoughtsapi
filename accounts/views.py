from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view  
# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    """adjust this api view to only accept uuid for querying instead of pk or id"""

    queryset =  UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_Calsses = [IsOwnerProfileOrReadOnly, IsAuthenticated]


@api_view(['GET'])
def list_location(request, pk):
  
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    if request.method == 'GET':
        location = UserProfile.objects.filter(id=pk)
        
        serializer = UserProfileSerializer(location, many=True)
        return Response(list(serializer.data)[0]['location'])
