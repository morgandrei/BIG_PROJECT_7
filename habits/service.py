from django_celery_beat.models import PeriodicTask, CrontabSchedule


def create_habits(habit):
    schedule, created = CrontabSchedule.objects.get_or_create(minute=habit.timing.minute,
                                                              hour=habit.timing.hour,
                                                              day_of_month=f'*/{habit.frequency}',
                                                              month_of_year='*',
                                                              day_of_week='*',
                                                              timezone='Europe/Moscow')
    PeriodicTask.objects.create(
        crontab=schedule,
        name='every_day',
        task='habits.tasks.every_day',
        args=[habit.id]
    )


def delete_habits(habit):
    task_name = 'every_day'  # такое же имя как в 13-строчке
    PeriodicTask.objects.filter(name=task_name).delete()


def update_habits(habit):
    delete_habits(habit)
    create_habits(habit)
