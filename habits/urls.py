from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitCreateView, HabitsListView, HabitsPablicListView, HabitDetailView, HabitUpdateView, \
    HabitDeleteView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateView.as_view(), name='habit-create'),
    path('list/', HabitsListView.as_view(), name='habits-list'),
    path('list/public/', HabitsPablicListView.as_view(), name='public_habit-list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit-get'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='habit-delete'),
]
