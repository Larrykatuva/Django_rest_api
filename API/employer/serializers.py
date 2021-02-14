from rest_framework import serializers
from django.contrib.auth.models import User


class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        filds = ('first_name',
                 'last_name',
                 'email',
                 'url')