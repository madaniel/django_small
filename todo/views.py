from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .form import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    todo_form = TodoForm()

    context = {'todo_list': todo_list, 'todo_form': todo_form}

    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    todo_form = TodoForm(request.POST)

    if todo_form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def complete_todo(request, todo_id):
    todo_task = Todo.objects.get(pk=todo_id)
    todo_task.complete = True

    todo_task.save()

    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()

    return redirect('index')
