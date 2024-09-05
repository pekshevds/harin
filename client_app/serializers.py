from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    is_reseller = serializers.BooleanField(required=False, allow_null=True)
    inn = serializers.IntegerField(required=False, allow_null=True)
