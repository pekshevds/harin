from django.urls import path
from pages_app.views import PageView


app_name = "pages_app"

urlpatterns = [
    path("", PageView.as_view(), name="page"),
]
