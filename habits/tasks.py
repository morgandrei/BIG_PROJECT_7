from datetime import datetime
import pytz
from celery import shared_task
from habits.models import Habits
from habits.andrei_habit_bot import handle


@shared_task
def every_day():
    timezone = pytz.timezone('Europe/Moscow')
    current_time_unf = datetime.now(timezone)
    current_time = current_time_unf.strftime('%H:%M')
    habits = Habits.objects.all()

    for habit in habits:
        if habit.DAILY:
            if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                handle(habit.get_habit)  # Выполняем отправку

        if habit.WEEKLY:
            if (current_time_unf - habit.create_time).days > 7:  # каждую неделю
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)  # Выполняем отправку
