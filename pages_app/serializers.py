from rest_framework import serializers


class PageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    seo_title = serializers.CharField(max_length=2048, required=False, allow_blank=True)
    seo_description = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
    seo_keywords = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
