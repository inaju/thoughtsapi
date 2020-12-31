from rest_framework import serializers
from .models import ThoughtModel
from accounts.models import UserProfile

class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThoughtModel
        fields = '__all__'
