from todos.forms import CreateTodoForm
from django.shortcuts import redirect, render
from .models import Person, Todo

def all_todos(request):
    if request == "Post":
        pass
    else:
        tasks = Todo.objects.all()
        context = {
            'todos': tasks,
            'form': CreateTodoForm(),
        }

        return render(request, 'index.html', context)

def create_todo(request):
    form = CreateTodoForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        description = form.cleaned_data['description']
        
        todo = Todo(
            text= text,
        
            description= description,
            )
        todo.save()
        return redirect('/')
    tasks = Todo.objects.all()
    context = {
            'todos': tasks,
            'form': CreateTodoForm(),
        }

    return render(request, 'index.html', context)
 