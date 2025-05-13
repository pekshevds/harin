from django.db import transaction
from django.db.models import QuerySet
from order_app.models import Organization


def organization_by_id(organization_id: str) -> Organization:
    return Organization.objects.filter(id=organization_id).first()


def handle_organization(organization_dict: dict) -> Organization:
    organization_id = organization_dict.get("id", None)
    organization_name = organization_dict.get("name", "")
    organization_inn = organization_dict.get("inn", "")
    organization = organization_by_id(organization_id)
    if organization is None:
        organization = Organization.objects.create(
            id=organization_id, name=organization_name
        )
    organization.name = organization_name
    organization.inn = organization_inn
    organization.save()
    return organization


def handle_organization_list(organization_list: list[dict]) -> QuerySet[Organization]:
    organization_id = []
    with transaction.atomic():
        for organization_item in organization_list:
            organization = handle_organization(organization_dict=organization_item)
            organization_id.append(organization.id)
    return Organization.objects.filter(id__in=organization_id)
