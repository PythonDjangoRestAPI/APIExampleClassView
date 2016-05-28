from rest_framework import serializers

from api.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('id','email')
