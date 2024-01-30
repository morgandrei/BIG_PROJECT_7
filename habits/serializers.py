from datetime import datetime

from rest_framework import serializers
from habits.models import Habits
from django import forms
from habits.validators import RelatedHabitValidator, PleasantHabitValidator, MinFrequencyValidator, \
    TimeDeltaHabitValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

        validators = [
            RelatedHabitValidator(fields=['related_habit']),
            PleasantHabitValidator(),
            MinFrequencyValidator(),
            TimeDeltaHabitValidator()
        ]


