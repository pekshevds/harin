from django.core.paginator import Paginator
from rest_framework import (
    permissions,
    authentication
)
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog_app.models import (
    Manufacturer,
    Good
)
from catalog_app.serializers import (
    ManufacturerSerializer,
    GoodSerializer
)
from catalog_app.services.good import (
    handle_good_list,
    fetch_goods_queryset_by_name_or_article
)
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.good import fetch_goods_queryset_by_filters
from catalog_app.services.update_catalog import update_catalog_from_json


class ManufacturerView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class GoodView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            queryset = None

            search = request.GET.get("search")
            if search:
                queryset = fetch_goods_queryset_by_name_or_article(search)
            else:
                manufacturers = None
                manufacturer_id = request.GET.get("manufacturer_id")
                if manufacturer_id:
                    manufacturers = manufacturer_by_id_list(
                        manufacturer_id.split(",")
                    )
                queryset = fetch_goods_queryset_by_filters(
                    manufacturers
                )

            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {
            "data": serializer.data,
            "count": len(queryset)
            }
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_good_list(good_list=data)
            serializer = GoodSerializer(queryset, many=True)
            response["data"] = serializer.data
        return Response(response)


class UpdateCatalogView(APIView):
    def post(self, request):
        update_catalog_from_json(request.data.get("data"))
        response = {"data": []}
        return Response(response)
