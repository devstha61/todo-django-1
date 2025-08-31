from django.http import HttpResponseRedirect
from django.shortcuts import render

from todo_app.models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "todo_list.html",
        {"todos": todos},
    )

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_create(request):
    print(request.method, request.POST)
    if request.method == "GET":
        return render(request, "todo_create.html")
    else:
        Todo.objects.create(title=request.POST['title'])
        return HttpResponseRedirect("/")