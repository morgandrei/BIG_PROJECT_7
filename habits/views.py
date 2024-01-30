from datetime import timedelta

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from habits.models import Habits
from habits.pagination import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
        # Добавить строчку расписания и задачи


class HabitsListView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return self.queryset
            return self.queryset.filter(owner=self.request.user)


class HabitsPablicListView(generics.ListAPIView):
    queryset = Habits.objects.all().filter(is_public=True)
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]


class HabitDetailView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        habit = serializer.save
        #  Добавить обновление


class HabitDeleteView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):
        # Удаление напоминания привычки
        instance.delete()
