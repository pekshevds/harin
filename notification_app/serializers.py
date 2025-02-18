from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=1024)
