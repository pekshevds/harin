from django.http import HttpResponse, HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from notification_app.commons import get_recipient_list
from notification_app.serializers import DataSerializer
from auth_app.transport import send_mail


def send_notification(
    subject: str, data: dict[str, str], recipient_list: list[str]
) -> HttpResponse:
    if not recipient_list:
        return Response(
            {"data": {"message": "empty recipient list"}}, status=status.HTTP_200_OK
        )
    ds = DataSerializer(data=data)
    if not ds.is_valid():
        return Response({"data": {"message": "bad data"}}, status=status.HTTP_200_OK)

    message = f"""Имя {ds.validated_data.get("name", "")}
        Почта {ds.validated_data.get("email", "")}
        Телефон {ds.validated_data.get("subject", "")}
        Сообщение {ds.validated_data.get("message", "")}
        """
    send_mail(subject, message, recipient_list)
    return Response({"data": ds.validated_data}, status=status.HTTP_200_OK)


class ProjectOrderView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        return send_notification(
            "Заказ проекта", request.data.get("data"), get_recipient_list()
        )


class OrderInstallationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        return send_notification(
            "Заказать монтаж", request.data.get("data"), get_recipient_list()
        )


class OnlineTrainingView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        return send_notification(
            "Онлайн обучение", request.data.get("data"), get_recipient_list()
        )


class ForDevelopersView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        return send_notification(
            "Застройщикам ИЖС", request.data.get("data"), get_recipient_list()
        )
