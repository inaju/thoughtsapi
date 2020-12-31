from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ThoughtModel
from .serializers import ThoughtSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .permissions import IsOwnerProfileOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from accounts.serializers import UserProfileSerializer
from django.http import HttpResponse

class ListThoughts(generics.ListCreateAPIView):
    queryset = ThoughtModel.objects.all()
    serializer_class = ThoughtSerializer

    def perform_create(self, ThoughtSerializer):
        #return print(self.request._request)
        ThoughtSerializer.save(owner=self.request.user)
