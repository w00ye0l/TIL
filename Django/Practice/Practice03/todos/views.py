from importlib.resources import contents
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos_ = Todo.objects.order_by("completed", "-priority")

    context = {
        "todos": todos_,
    }

    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content___")
    priority = request.GET.get("priority___")
    deadline = request.GET.get("deadline___")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todos:index")


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    todo.completed = not todo.completed

    todo.save()

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")
