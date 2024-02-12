from rest_framework.serializers import ValidationError
from django.utils import timezone


class NotRewardAndRelhabValidator:
    """Валидация: нельзя одновременно указывать связанную привычку и вознаграждение"""

    def __call__(self, value):
        related_habit = value.get('related_habit')
        reward = value.get('reward')
        if related_habit and reward:
            raise ValidationError('Нельзя одновременно указывать связанную привычку и вознаграждение!')
        return value


class TimeDeltaHabitValidator:
    """Валидация: время выполнения привычки не должно превышать 120 секунд"""

    def __call__(self, value):
        time_to_perform = value.get('time_to_perform')
        if time_to_perform > 120:
            raise ValidationError('Время выполнения привычки не должно превышать 120 секунд!')
        return value


class PleasantHabitValidator:
    """Валидация: у приятной привычки не может быть вознаграждения или связанной привычки."""

    def __call__(self, value):
        is_pleasurable = value.get('is_pleasurable')
        reward = value.get('reward')
        related_habit = value.get('related_habit')

        if is_pleasurable:
            if reward:
                raise ValidationError('Приятная привычка не может иметь вознаграждение.')
            if related_habit:
                raise ValidationError('Приятная привычка не может иметь связанную привычку.')
        return value


class RelatedHabitValidator:
    """Валидация: связанная привычка должна быть приятной"""

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            related_habit = value.get(field)
            if related_habit:
                if related_habit and not related_habit.is_pleasurable:
                    raise ValidationError('Связанная привычка должна быть приятной')


class MinFrequencyValidator:
    """Валидация: нельзя выполнять привычку реже 1 раза в неделю"""

    def __call__(self, value):
        frequency = value.get('frequency')
        if frequency == 'Еженедельная':
            time_to_perform = value.get('time_to_perform')
            if time_to_perform:
                difference = (timezone.now() - time_to_perform).days
                if difference < 7:
                    raise ValidationError('Привычку нельзя выполнять реже, чем 1 раз в 7 дней.')
        return value
