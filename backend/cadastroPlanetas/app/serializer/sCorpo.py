from rest_framework import serializers

from app.models.CorpoModel import Corpo


class CorpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corpo
        fields = '__all__'
