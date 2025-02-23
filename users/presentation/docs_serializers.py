from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    email = serializers.EmailField(required=True)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()
    ci = serializers.CharField()
    email = serializers.EmailField()


class VerifyMailSerializer(serializers.Serializer):
    email = serializers.CharField()
    token = serializers.CharField()
