from rest_framework import serializers

from business_api import models


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer a business user object"""
    class Meta:
        model = models.Business
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.Business.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class BusinessFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BusinessFeedItem
        fields = ('id', 'business', 'status_text', 'created_on')
        extra_kwargs = {'business': {'read_only': True}}
