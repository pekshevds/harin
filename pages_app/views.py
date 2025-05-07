from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from pages_app.models import Page
from pages_app.serializers import PageSerializer


class PageView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
