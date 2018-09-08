import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseServerError
from django.views import generic
from . import models, forms


def step1or2(request, num):
    todos = models.Todo.objects.all().order_by("due")
    my_context = {
        "todos":todos,
        }
    return render(request, "todo/step"+num+".html", my_context)


def step4(request):
    if request.method == "POST":
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:step1or2", num=1)
    else:
        form = forms.TodoForm()
    todos = models.Todo.objects.all().order_by("due")
    my_context = {
        "form":form,
        "todos":todos,
        }
    return render(request, "todo/step4.html", my_context)


def get_todo(request):
    todos = models.Todo.objects.all().order_by("due").values()
    todolist = list(todos)
    return JsonResponse(todolist, safe=False)


def post_todo(request):
    if request.method == 'POST' and request.body:
        json_dict = json.loads(request.body)
        task = json_dict['task']
        due = json_dict['due']
        done = json_dict['done']
        todos = models.Todo.objects.filter(task=task)
        if not todos:
            models.Todo.objects.create(task=task, due=due, done=done);
        else:
            todos[0].due=due
            todos[0].done=done
            todos[0].save()
        return JsonResponse(json_dict)
    else:
        return HttpResponseServerError()
