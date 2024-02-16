from django.urls import path
from catalog_app.views import (
    ManufacturerView,
    GoodView,
    UpdateCatalogView
)


app_name = 'catalog_app'

urlpatterns = [
    path('manufacturer/', ManufacturerView.as_view(), name="manufacturer"),
    path('good/', GoodView.as_view(), name="good"),
    path('update-catalog/', UpdateCatalogView.as_view(), name="update-catalog"),
]
