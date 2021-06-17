from todos.forms import CreateTodo
from django.shortcuts import render
from .models import Todo

def todos(request):
    tasks = Todo.objects.all()
    context = {
        'todos': tasks,
    }

    return render(request, 'index.html', context)
