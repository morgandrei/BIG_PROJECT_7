from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MyAPITestCase(APITestCase):
    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.url = reverse('schema-swagger-ui')

    def test_get(self):
        # Тестирование GET-запроса к API
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
