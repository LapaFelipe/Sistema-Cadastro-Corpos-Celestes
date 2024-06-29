from rest_framework import serializers

from app.models.UserModel import UserManager, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance