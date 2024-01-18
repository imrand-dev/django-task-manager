from rest_framework import serializers

from account.models import User
from account.services.users import UserService

user_service = UserService()


class PublicUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User 
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
            "email",
            "password",
            "avatar",
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
            "is_active",
            "is_verified"
        ]
    
    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(**validated_data)
        user.set_password(password)

        user.save()
        return user