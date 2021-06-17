from todos.views import todos
from django.urls import path


urlpatterns = [
    path('', todos, name='index')
]