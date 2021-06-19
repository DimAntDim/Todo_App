from todos.forms import CreateTodo
from django.shortcuts import redirect, render
from .models import Todo

def all_todos(request):
    if request == "Post":
        pass
    else:
        tasks = Todo.objects.all()
        form = CreateTodo()
        context = {
            'todos': tasks,
            'form': form,
        }

        return render(request, 'index.html', context)

def create_todo(request):
    creator = request.POST['creator']
    description = request.POST['description']
    todo = Todo(
        creator=creator,
        description=description,
        )
    todo.save()
    return redirect('/') 
