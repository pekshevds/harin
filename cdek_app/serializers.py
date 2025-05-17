from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True, allow_null=False)


class PackageSerializer(serializers.ListField):
    weight = serializers.IntegerField(required=True, allow_null=False)
    length = serializers.IntegerField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()


class StringListField(serializers.ListField):
    child = serializers.CharField()


class PhoneListField(serializers.ListField):
    number = serializers.CharField(max_length=24, required=True, allow_null=False)
    additional = serializers.CharField(max_length=255, required=True, allow_null=False)


class WorkTimelistField(serializers.ListField):
    day = serializers.IntegerField(required=True, allow_null=False)
    time = serializers.CharField(max_length=255, required=True, allow_null=False)


class LocationField(serializers.Serializer):
    country_code = serializers.CharField(max_length=2, required=True, allow_null=False)
    region_code = serializers.IntegerField(required=True, allow_null=False)
    region = serializers.CharField(max_length=255, required=True, allow_null=False)
    city_code = serializers.IntegerField(required=True, allow_null=False)
    city = serializers.CharField(max_length=255, required=True, allow_null=False)
    longitude = serializers.FloatField(required=True, allow_null=False)
    latitude = serializers.FloatField(required=True, allow_null=False)
    address = serializers.CharField(max_length=255, required=True, allow_null=False)
    address_full = serializers.CharField(
        max_length=255, required=True, allow_null=False
    )


class DeliveryModesListField(serializers.ListField):
    delivery_mode = serializers.CharField(max_length=255)
    delivery_mode_name = serializers.CharField(max_length=255)
    tariff_code = serializers.IntegerField()


class AdditionalOrderTypesParamSerializer(serializers.Serializer):
    without_additional_order_type = serializers.BooleanField()
    additional_order_types = serializers.ListField(child=serializers.CharField())


class TariffCodesListField(serializers.ListField):
    tariff_name = serializers.CharField(max_length=255)
    weight_min = serializers.FloatField()
    weight_max = serializers.FloatField()
    weight_calc_max = serializers.FloatField()
    length_min = serializers.IntegerField()
    length_max = serializers.IntegerField()
    width_min = serializers.IntegerField()
    width_max = serializers.IntegerField()
    height_min = serializers.IntegerField()
    height_max = serializers.IntegerField()
    order_types = serializers.ListField(child=serializers.CharField())
    payer_contragent_type = serializers.ListField(child=serializers.CharField())
    sender_contragent_type = serializers.ListField(child=serializers.CharField())
    recipient_contragent_type = serializers.ListField(child=serializers.CharField())
    delivery_modes = DeliveryModesListField()
    additional_order_types_param = AdditionalOrderTypesParamSerializer()


class TariffListResponceListField(serializers.ListField):
    tariff_code = serializers.IntegerField(required=True, allow_null=False)
    tariff_name = serializers.CharField(max_length=255, required=True, allow_null=False)
    delivery_mode = serializers.IntegerField(required=True, allow_null=False)
    delivery_sum = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=True, allow_null=False
    )
    period_min = serializers.IntegerField(required=True, allow_null=False)
    period_max = serializers.IntegerField(required=True, allow_null=False)


class CDEKRegionSerializer(serializers.Serializer):
    region = serializers.CharField(max_length=255, required=True, allow_null=False)
    region_code = serializers.IntegerField()
    country = serializers.CharField(max_length=255, required=True, allow_null=False)
    country_code = serializers.CharField(max_length=2, required=True, allow_null=False)


class CDEKCitySerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True, allow_null=False)
    city_uuid = serializers.CharField(max_length=36, required=True, allow_null=False)
    city = serializers.CharField(max_length=255, required=True, allow_null=False)
    fias_guid = serializers.CharField(max_length=36)
    kladr_code = serializers.CharField(max_length=36)
    country_code = serializers.CharField(max_length=2, required=True, allow_null=False)
    country = serializers.CharField(max_length=255, required=True, allow_null=False)
    region = serializers.CharField(max_length=255, required=True, allow_null=False)
    region_code = serializers.IntegerField()
    sub_region = serializers.CharField(max_length=255)
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    time_zone = serializers.CharField(max_length=255)
    payment_limit = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=True, allow_null=False
    )


class CDEKPostalCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True, allow_null=False)
    postal_codes = StringListField(required=True, allow_null=False)


class CDEKSuggestCitySerializer(serializers.Serializer):
    city_uuid = serializers.CharField(max_length=36, required=True, allow_null=False)
    code = serializers.IntegerField(required=True, allow_null=False)
    full_name = serializers.CharField(max_length=255, required=True, allow_null=False)


class CDEKDeliverypointsSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, required=True, allow_null=False)
    uuid = serializers.CharField(max_length=255, required=True, allow_null=False)
    work_time = serializers.CharField(max_length=255, required=True, allow_null=False)
    phones = PhoneListField(required=True, allow_null=False)
    type = serializers.CharField(max_length=255, required=True, allow_null=False)
    owner_code = serializers.CharField(max_length=255, required=True, allow_null=False)
    take_only = serializers.BooleanField(required=True, allow_null=False)
    is_handout = serializers.BooleanField(required=True, allow_null=False)
    is_reception = serializers.BooleanField(required=True, allow_null=False)
    is_dressing_room = serializers.BooleanField(required=True, allow_null=False)
    have_cashless = serializers.BooleanField(required=True, allow_null=False)
    have_cash = serializers.BooleanField(required=True, allow_null=False)
    have_fast_payment_system = serializers.BooleanField(required=True, allow_null=False)
    allowed_cod = serializers.BooleanField(required=True, allow_null=False)
    work_time_list = WorkTimelistField(required=True, allow_null=False)
    location = LocationField(required=True, allow_null=False)


class CDEKAllTariffsSerializer(serializers.Serializer):
    tariff_codes = TariffCodesListField()


class CDEKTariffListRequestSerializer(serializers.Serializer):
    from_location = LocationSerializer()
    to_location = LocationSerializer()
    packages = PackageSerializer()


class CDEKTariffListResponceSerializer(serializers.Serializer):
    tariff_codes = TariffListResponceListField()


class CDEKTariffRequestSerializer(CDEKTariffListRequestSerializer):
    tariff_code = serializers.IntegerField(required=True, allow_null=False)


class CDEKTariffResponceSerializer(serializers.Serializer):
    delivery_sum = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=True, allow_null=False
    )
    period_min = serializers.IntegerField(required=True, allow_null=False)
    period_max = serializers.IntegerField(required=True, allow_null=False)
    weight_calc = serializers.IntegerField(required=True, allow_null=False)
    total_sum = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=True, allow_null=False
    )
    currency = serializers.CharField(max_length=25, required=True, allow_null=False)
