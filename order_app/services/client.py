from django.db import transaction
from django.db.models import QuerySet
from order_app.models import Client


def client_by_id(client_id: str) -> Client:
    return Client.objects.filter(id=client_id).first()


def handle_client(client_diсt: dict) -> Client:
    client_id = client_diсt.get("id", None)
    client_name = client_diсt.get("name", "")
    client = client_by_id(client_id)
    if client is None:
        client = Client.objects.create(id=client_id, name=client_name)
    client.name = client_name
    client.save()
    return client


def handle_client_list(client_list: list[dict]) -> QuerySet[Client]:
    client_id = []
    with transaction.atomic():
        for client_item in client_list:
            client = handle_client(client_diсt=client_item)
            client_id.append(client.id)
    return Client.objects.filter(id__in=client_id)
