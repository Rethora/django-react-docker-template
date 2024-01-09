from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        """
        Meta class for defining metadata options for the User serializer.
        """

        model = User
        fields = ["url", "username", "email", "groups", "is_staff"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Group model.
    """

    class Meta:
        """
        Meta class for defining metadata options for the serializer.
        """

        model = Group
        fields = ["url", "name"]
