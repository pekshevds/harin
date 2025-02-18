from django.urls import path
from notification_app.views import (
    ProjectOrderView,
    OrderInstallationView,
    OnlineTrainingView,
    ForDevelopersView,
)

app_name = "notification_app"

urlpatterns = [
    path("project-order/", ProjectOrderView.as_view(), name="project-order"),
    path(
        "order-installation/",
        OrderInstallationView.as_view(),
        name="order-installation",
    ),
    path("online-training/", OnlineTrainingView.as_view(), name="online-training"),
    path("for-developers/", ForDevelopersView.as_view(), name="for-developers"),
]
