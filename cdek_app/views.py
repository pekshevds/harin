from typing import Any
from rest_framework import permissions

# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpRequest
from cdek_app.serializers import (
    CDEKRegionSerializer,
    CDEKCitySerializer,
    CDEKPostalCodeSerializer,
    CDEKSuggestCitySerializer,
    CDEKDeliverypointsSerializer,
    CDEKAllTariffsSerializer,
    CDEKTariffListRequestSerializer,
    CDEKTariffListResponceSerializer,
    CDEKTariffRequestSerializer,
    CDEKTariffResponceSerializer,
)
from cdek_app.fetchers import (
    fetch_cdek_regions,
    fetch_cdek_cities,
    fetch_cdek_postalcodes,
    fetch_cdek_suggestcities,
    fetch_cdek_deliverypoints,
    fetch_cdek_alltariffs,
    fetch_cdek_tarifflist,
    fetch_cdek_tariff,
)


class CDEKRegionsView(APIView):
    """Регионы"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        serializer = CDEKRegionSerializer(fetch_cdek_regions(), many=True)
        response = {"data": serializer.data}
        return Response(response)


class CDEKСitiesView(APIView):
    """Населенные пункты"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest, region_code: int) -> HttpResponse:
        serializer = CDEKCitySerializer(fetch_cdek_cities(region_code), many=True)
        response = {"data": serializer.data}
        return Response(response)


class CDEKPostalCodesView(APIView):
    """Почтовые индексы"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest, city_code: int) -> HttpResponse:
        serializer = CDEKPostalCodeSerializer(fetch_cdek_postalcodes(city_code))
        response = {"data": serializer.data}
        return Response(response)


class CDEKSuggestCitiesView(APIView):
    """Писк населенных пунктов по названию"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        name = request.GET.get("name", "")
        if not name:
            return Response({"data": []})
        serializer = CDEKSuggestCitySerializer(
            fetch_cdek_suggestcities(name), many=True
        )
        response = {"data": serializer.data}
        return Response(response)


class CDEKDeliveryPointsView(APIView):
    """Получение списка офисов"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest, city_code: int) -> HttpResponse:
        serializer = CDEKDeliverypointsSerializer(
            fetch_cdek_deliverypoints(city_code), many=True
        )
        response = {"data": serializer.data}
        return Response(response)


class CDEKAllTariffsView(APIView):
    """Получение списка тарифов"""

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        serializer = CDEKAllTariffsSerializer(fetch_cdek_alltariffs())
        response = {"data": serializer.data}
        return Response(response)


class CDEKTariffListView(APIView):
    """Расчет по доступным тарифам"""

    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        response: dict[str, Any] = {"data": []}
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = CDEKTariffListRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer = CDEKTariffListResponceSerializer(fetch_cdek_tarifflist(data))
        response = {"data": serializer.data}
        return Response(response)


class CDEKTariffView(APIView):
    """Расчет по коду тарифа"""

    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest, tariff_code: int) -> HttpResponse:
        response: dict[str, Any] = {"data": []}
        data = request.data.get("data")
        if not data:
            return Response(response)
        data["tariff_code"] = tariff_code
        serializer = CDEKTariffRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer = CDEKTariffResponceSerializer(fetch_cdek_tariff(data))
        response = {"data": serializer.data}
        return Response(response)
