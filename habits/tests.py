from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from faker import Faker
from habits.models import Habits
from users.models import User
from habits.serializers import HabitsSerializer


class HabitAPITestCase(APITestCase):
    def setUp(self):
        # Подготовка данных перед тестом
        self.random_data = Faker()
        self.user = User.objects.create(
            email='admin@list.ru',
            password='0000',
            is_superuser=True
        )
        self.client.force_authenticate(user=self.user)

    def create_random_habit(self):
        return Habits.objects.create(
            owner=self.user,
            place=self.random_data.word(),
            timing=self.random_data.time(),
            action=self.random_data.word(),
            is_pleasurable=self.random_data.boolean(),
            frequency=Habits.Frequency.DAILY,
            reward=self.random_data.sentence(),
            time_to_perform=40,
            is_public=self.random_data.boolean()
        )

    def test_create_habit(self):
        user = self.user
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        data = {
            "owner": user.pk,
            "place": self.random_data.word(),
            "timing": self.random_data.time(),
            "action": self.random_data.word(),
            "is_pleasurable": self.random_data.boolean(),
            "frequency": Habits.Frequency.DAILY,
            "reward": None,
            "time_to_perform": 40,
            "is_public": self.random_data.boolean()
        }

        serializer = HabitsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()  # Сохранение объекта, если данные действительны

        response = self.client.post(reverse("habits:habit-create"), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.count(), 2)

    def test_list_habit(self):
        user = self.user
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Создание нескольких случайных привычек
        for random_habit in range(5):
            self.create_random_habit()

        response = self.client.get(reverse('habits:habits-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


    def test_update_habit(self):
        """Обновлениe привычки"""
        user = self.user
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        habit = self.create_random_habit()
        data = {
            "place": self.random_data.word(),
            "action": self.random_data.word(),
            "time_to_perform": 50
        }
        response = self.client.patch(reverse('habits:habit-update', args=[habit.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.place, data["place"])
        self.assertEqual(habit.action, data["action"])
        self.assertEqual(habit.time_to_perform, data["time_to_perform"])

    def test_delete_habit(self):
        user = self.user
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        habit = self.create_random_habit()
        response = self.client.delete(reverse('habits:habit-delete', args=[habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.count(), 0)
