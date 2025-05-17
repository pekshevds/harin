from django.urls import path
from cdek_app.views import (
    CDEKRegionsView,
    CDEKСitiesView,
    CDEKPostalCodesView,
    CDEKSuggestCitiesView,
    CDEKDeliveryPointsView,
    CDEKAllTariffsView,
    CDEKTariffListView,
    CDEKTariffView,
)

app_name = "cdek_app"

urlpatterns = [
    path("location/regions/", CDEKRegionsView.as_view(), name="regions"),
    path(
        "location/regions/<int:region_code>/cities/",
        CDEKСitiesView.as_view(),
        name="cities",
    ),
    path(
        "location/cities/",
        CDEKSuggestCitiesView.as_view(),
        name="suggestcities",
    ),
    path(
        "location/cities/<int:city_code>/postalcodes/",
        CDEKPostalCodesView.as_view(),
        name="postalcodes",
    ),
    path(
        "location/cities/<int:city_code>/deliverypoints/",
        CDEKDeliveryPointsView.as_view(),
        name="deliverypoints",
    ),
    path(
        "calculator/alltariffs/",
        CDEKAllTariffsView.as_view(),
        name="alltariffs",
    ),
    path(
        "calculator/calculate/",
        CDEKTariffListView.as_view(),
        name="tarifflist",
    ),
    path(
        "calculator/calculate/<int:tariff_code>/",
        CDEKTariffView.as_view(),
        name="tariff",
    ),
]
