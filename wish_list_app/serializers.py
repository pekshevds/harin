from rest_framework import serializers
from catalog_app.serializers import GoodSerializer


class WishListSerializer(serializers.Serializer):
    good = GoodSerializer()


class SimpleWishListSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
