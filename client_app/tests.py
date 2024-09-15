from django.test import TestCase
from client_app.models import Client


class TestClient(TestCase):
    def setUp(self) -> None:
        pass
        # self.client1 = Client.objects.create(name="client1", is_group=False, is_reseller=False)

    def test_create_simple_buyer(self):
        client = Client.objects.create(name="client1")
        self.assertFalse(client.is_reseller)

    def test_create_corp_buyer(self):
        client = Client.objects.create(name="client1", is_reseller=True)
        self.assertTrue(client.is_reseller)
