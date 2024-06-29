from app.models.CiePesqModel import CiePesq
from rest_framework import serializers


class CiePesqSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiePesq
        fields = '__all__'