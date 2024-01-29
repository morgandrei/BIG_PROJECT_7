from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from habits.models import Habits
from habits.serializers import HabitsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import Is


class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [Is]

