from todos.models import Todo
from django.contrib import admin


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    display = ['creator', 'date', 'descriptopn']

