from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import GENDER_SELECTION


class CustomRegisterSerializer(RegisterSerializer):
    avatar = serializers.ImageField() # upload_to='static/media')
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.avatar = self.data.get('avatar')
        user.gender = self.data.get('gender')
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.email = self.data.get('email')
        user.save()
        return user
        
