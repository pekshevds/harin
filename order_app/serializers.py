from rest_framework import serializers
from catalog_app.serializers import GoodSerializer
from client_app.serializers import ClientSerializer


class AuthorSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False, allow_null=True)
    email = serializers.EmailField()
    is_reseller = serializers.BooleanField(required=False, allow_null=True)


class CustomerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    inn = serializers.CharField(max_length=12)


class OrganizationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    inn = serializers.CharField(max_length=12)


class ContractSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=25)
    date = serializers.DateField(format="%Y-%m-%d")
    client = ClientSerializer()
    customer = CustomerSerializer()
    organization = OrganizationSerializer()


class SimpleContractSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=25)
    date = serializers.DateField(format="%Y-%m-%d")
    client_id = serializers.UUIDField()
    customer_id = serializers.UUIDField()
    organization_id = serializers.UUIDField()


class ItemOrderSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, required=False)
    good = GoodSerializer(read_only=True, required=False)
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    summ = serializers.DecimalField(max_digits=15, decimal_places=2)


class SimpleItemOrderSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, required=False)
    order_id = serializers.UUIDField(read_only=True, required=False)
    good_id = serializers.UUIDField(read_only=True, required=False)
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    summ = serializers.DecimalField(max_digits=15, decimal_places=2)


class OrderSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    number = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(format="%Y-%m-%d")
    contract = ContractSerializer()
    items = ItemOrderSerializer(many=True)
    author = AuthorSerializer()
    uploaded_at = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True, required=False
    )
    comment = serializers.CharField(max_length=None, required=False)


class SimpleOrderSerializer(serializers.Serializer):
    number = serializers.IntegerField(read_only=True, required=False)
    date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True, required=False)
    contract_id = serializers.UUIDField(required=False)
    items = SimpleItemOrderSerializer(many=True, required=False)
    uploaded_at = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True, required=False
    )
    comment = serializers.CharField(max_length=None, required=False)


class SimpleOrderWithoutClientSerializer(serializers.Serializer):
    number = serializers.IntegerField(read_only=True, required=False)
    date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True, required=False)
    name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=255, required=False)
    items = SimpleItemOrderSerializer(many=True, required=False)
    uploaded_at = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True, required=False
    )
    comment = serializers.CharField(max_length=None, required=False)
