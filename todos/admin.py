from todos.models import Person, Todo
from django.contrib import admin


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    display = ['owner', 'date', 'descriptopn']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    display = ['name']
