from rest_framework import serializers
from .models import period3
from django.contrib.auth.models import User

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('username','id')
        
