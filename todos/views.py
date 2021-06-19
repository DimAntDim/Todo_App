from todos.forms import CreateTodo
from django.shortcuts import redirect, render
from .models import Person, Todo

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
    task_name = request.POST['task-name']
    owner_name = request.POST['owner']
    description = request.POST['description']
    owner = Person.objects.filter(name=owner_name).first()

    if not owner:
        owner = Person(
            name=owner_name,
        )
        owner.save()

    todo = Todo(
        task_name= task_name,
        owner=owner,
        description= description,
        )
    todo.save()
    return redirect('/') 

