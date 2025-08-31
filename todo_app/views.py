from django.shortcuts import render

from todo_app.models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "todo_list.html",
        {"todos": todos},
    )