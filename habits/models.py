from datetime import timedelta
from django.db import models
from users.models import User, NULLABLE


class Habits(models.Model):

    class Frequency(models.TextChoices):
        DAILY = 'daily', 'Ежедневно'
        WEEKLY = 'weekly', 'Ежемесячно'
        CUSTOM = 'monthly', 'Настраиваемое'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')  # Создатель привычки.
    place = models.CharField(max_length=25, verbose_name='место выполнения привычки')
    timing = models.TimeField(verbose_name='время выполнения привычки')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasurable = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.CharField(choices=Frequency.choices, verbose_name='периодичность')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    time_to_perform = models.DurationField(max_length=timedelta(seconds=120), verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.timing} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
