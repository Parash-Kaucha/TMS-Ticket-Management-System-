from .models import User
from rest_framework import serializers
from authentication.models import User

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    phone_number = serializers.CharField(allow_null=False, allow_blank=False, min_length=10, max_length=14)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Username already exists")

        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="Already registered with this email.")
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user