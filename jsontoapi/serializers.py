from rest_framework import serializers
from .models import *

class user1serializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = '__all__'