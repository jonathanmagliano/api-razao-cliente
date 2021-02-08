from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):

    creationDate = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('profile', 'username', 'password', 'name', 'email', 'location', 'creationDate')
        extra_kwargs = {'password': {'write_only': True}}
