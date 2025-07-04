from django.urls import path
from order_app.views import (
    ContractView,
    OrderView,
    OrderWithoutAuthorView,
    OrderRainBlockRuView,
    OrderItemView,
    MakrOrderView,
    NewOrdersView,
)
from client_app.views import ClientView

app_name = "order_app"

urlpatterns = [
    path("", OrderView.as_view(), name="order"),
    path("without-author/", OrderWithoutAuthorView.as_view(), name="without-author"),
    path(
        "rain-block-ru/",
        OrderRainBlockRuView.as_view(),
        name="rain-block-ru",
    ),
    path("item/", OrderItemView.as_view(), name="order-item"),
    path("contract/", ContractView.as_view(), name="contract"),
    path("client/", ClientView.as_view(), name="client"),
    path("mark-order/", MakrOrderView.as_view(), name="mark-order"),
    path("new-orders/", NewOrdersView.as_view(), name="new-orders"),
]
