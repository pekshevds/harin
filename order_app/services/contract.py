"""from datetime import datetime"""

from django.db import transaction
from django.db.models import QuerySet
from order_app.models import Contract
from order_app.services.customer import handle_customer
from order_app.services.organization import handle_organization
from order_app.services.client import handle_client


def contract_by_id(contract_id: str) -> Contract:
    return Contract.objects.filter(id=contract_id).first()


def handle_contract(contract_dict: dict) -> Contract:
    contract_id = contract_dict.get("id", None)
    contract_name = contract_dict.get("name", "")
    contract_number = contract_dict.get("number", "")
    contract_date = contract_dict.get("date", None)
    """if contract_date:
        contract_date = datetime.strptime(contract_date, '%Y-%m-%d')"""
    contract = contract_by_id(contract_id)
    if contract is None:
        contract = Contract.objects.create(id=contract_id, name=contract_name)
    contract.number = contract_number
    contract.date = contract_date
    key_name = "customer"
    if key_name in contract_dict:
        temp_dir = contract_dict.get(key_name)
        contract.customer = None if temp_dir is None else handle_customer(temp_dir)
    key_name = "organization"
    if key_name in contract_dict:
        temp_dir = contract_dict.get(key_name)
        contract.organization = (
            None if temp_dir is None else handle_organization(temp_dir)
        )
    key_name = "client"
    if key_name in contract_dict:
        temp_dir = contract_dict.get(key_name)
        contract.client = None if temp_dir is None else handle_client(temp_dir)
    contract.save()
    return contract


def handle_contract_list(contract_list: list[dict]) -> QuerySet[Contract]:
    contract_id = []
    with transaction.atomic():
        for contract_item in contract_list:
            contract = handle_contract(contract_dict=contract_item)
            contract_id.append(contract.id)
    return Contract.objects.filter(id__in=contract_id)
