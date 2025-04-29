import logging
from datetime import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import permissions, authentication
from order_app.models import Contract, Order, ItemOrder
from order_app.serializers import (
    ContractSerializer,
    SimpleOrderSerializer,
    OrderSerializer,
    ItemOrderSerializer,
    SimpleItemOrderSerializer,
    SimpleOrderWithoutClientSerializer,
)
from order_app.services.order import handle_order_list, order_by_id

default_number_of_page = 1
item_count_per_page = 5
logger = logging.getLogger(__name__)


class ContractView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        queryset = Contract.objects.filter(client=client)
        serializer = ContractSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        order = order_by_id(order_id=request.GET.get("id"))
        total = 0
        if order:
            queryset = [order]
            total = 1
        else:
            if client:
                queryset = Order.objects.filter(client=client)
            else:
                queryset = Order.objects.filter(author=request.user)
            page_number = request.GET.get("page", default_number_of_page)
            count = request.GET.get("count", item_count_per_page)
            total = len(queryset)  # total orders by author or client
            paginator = Paginator(queryset, count)
            queryset = paginator.get_page(page_number)
        serializer = OrderSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "total": total,
            "success": True,
        }
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data")
        if not data:
            return Response(response)
        logger.info({"order_data": data})
        serializer = SimpleOrderSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_order_list(order_list=data, author=request.user)
            serializer = OrderSerializer(queryset, many=True)
            response["data"] = serializer.data
            response["success"] = True
        return Response(response)


class OrderWithoutAuthorView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data")
        if not data:
            return Response(response)
        logger.info({"order_data": data})
        serializer = SimpleOrderWithoutClientSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_order_list(order_list=data, author=None)
            serializer = OrderSerializer(queryset, many=True)
            response["data"] = serializer.data
            response["success"] = True
        return Response(response)


class OrderDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = get_object_or_404(Order, id=request.GET.get("id"))
        order.delete()
        response = {"data": []}
        return Response(response)


class OrderItemView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = get_object_or_404(Order, id=request.GET.get("id"))
        serializer = SimpleItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderItemDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        item = get_object_or_404(ItemOrder, id=request.GET.get("id"))
        order = item.order
        item.delete()
        serializer = ItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data}
        return Response(response)


class NewOrdersView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Order.objects.filter(uploaded_at=None)
        serializer = OrderSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "total": len(queryset),
            "success": True,
        }
        return Response(response)


class MakrOrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = get_object_or_404(Order, id=request.GET.get("id"))
        order.uploaded_at = datetime.now()
        order.save()
        return Response({"data": {"marked": True}}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.get("data")
        if not data:
            return Response({"data": {"empty data": True}}, status=status.HTTP_200_OK)
        now = datetime.now()
        for item in data:
            try:
                order = get_object_or_404(Order, id=item)
                order.uploaded_at = now
                order.save()
            except Http404:
                pass
            except ValueError:
                pass
        return Response({"data": {"marked": True}}, status=status.HTTP_200_OK)
