from django.http import HttpResponseRedirect
from django.shortcuts import render

from todo_app.models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos},
    )

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_create(request):
    print(request.method, request.POST)
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
        Todo.objects.create(title=request.POST['title'])
        return HttpResponseRedirect("/")
    
def todo_update(request, id):
    if request.method == "GET":
        todo = Todo.objects.get(id=id)
        return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo},
        )
    else:
        todo=Todo.objects.get(id=id)
        todo.title = request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/")