from django.test import TestCase
from rest_framework.authtoken.models import Token
from auth_app.models import User
from client_app.models import Client
from catalog_app.models import Good
from order_app.models import Order, ItemOrder, Organization, Contract, Customer


class TestOrder(TestCase):
    def setUp(self) -> None:
        self._client = Client.objects.create(name="client1")
        self.user = User.objects.create(email="mail@mail.ru", client=self._client)
        self.organization = Organization.objects.create(name="org1")
        self.customer = Customer.objects.create(name="cust1")
        self.contract = Contract.objects.create(
            name="cont1",
            client=self._client,
            customer=self.customer,
            organization=self.organization,
        )
        self.token = Token.objects.create(user=self.user)
        self.good1 = Good.objects.create(name="good1", balance=1, price1=50, price2=75)

    def test_create_order(self):
        order = Order.objects.create(contract=self.contract)
        ItemOrder.objects.create(
            order=order,
            good=self.good1,
            quantity=self.good1.balance,
            price=self.good1.price1,
            summ=self.good1.price1 * self.good1.balance,
        )
        self.assertNotEqual(order, None)

    def test_create_order_api(self):
        data = {
            "contract_id": self.contract.id,
            "items": [
                {
                    "good_id": self.good1.id,
                    "quantity": self.good1.balance,
                    "price": self.good1.price1,
                    "summ": self.good1.balance * self.good1.price1,
                },
            ],
        }
        resp = self.client.post(
            "/api/v1/order",
            headers={"Authorization": f"Token {self.token}"},
            data=data,
        )
        self.assertTrue(resp.status_code in [301, 200])

    def test_create_order_by_api(self):
        data = {
            "contract_id": self.contract.id,
            "items": [
                {
                    "good_id": self.good1.id,
                    "quantity": self.good1.balance,
                    "price": self.good1.price1,
                    "summ": self.good1.balance * self.good1.price1,
                },
            ],
        }
        response = self.client.post(
            "/api/v1/order",
            headers={"Authorization": f"Token {self.token}"},
            data=data,
        )
        self.assertTrue(response.status_code in [301, 200])
        order = Order.objects.filter(author=self.user).first()
        print(order)
        # print(dir(response))
        # print("content:", response.content)
        # self.assertIsNotNone(resp.get("data", None))
        # self.assertTrue(resp.data."success"])
