from todos.views import all_todos, create_todo
from django.urls import path


urlpatterns = [
    path('', all_todos, name='index'),
    path('create', create_todo, name='create'),
]