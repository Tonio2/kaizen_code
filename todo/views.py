from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Todo

def check_input(input):
    bd_input = input.split(' ')
    if len(bd_input) < 2:
        return "Usage : cmd todo_title"
    cmd = bd_input[0]
    todo_title = ' '.join(bd_input[1:])
    if cmd not in ["add", "done", "del"]:
        return "Allowed cmds : add, done, del"
    if len(todo_title) == 0:
        return "todo_title must contain at least one character"
    if cmd == "add":
        if len(Todo.objects.filter(todo_title = todo_title)) > 0:
            return "Todo " + todo_title + " has already been created"
        todo = Todo(todo_title = todo_title)
        todo.save()
        return "ok"
    if cmd == "del":
        if len(Todo.objects.filter(todo_title = todo_title)) == 0:
            return "Todo " + todo_title + " does not exist"
        Todo.objects.filter(todo_title = todo_title).delete()
        return "ok"
    if cmd == "done":
        if len(Todo.objects.filter(todo_title = todo_title)) == 0:
            return "Todo " + todo_title + " does not exist"
        todo = Todo.objects.filter(todo_title = todo_title)
        todo.done = True
        todo.save()
        return "ok"

def index(request):
    todos = Todo.objects.all()
    context = {'todos' : todos}
    return render(request, 'todo/index.html', context)

def parse_input(request):
    input = request.POST['input']
    print(input)
    exit_code = check_input(input)
    print(exit_code)
    if exit_code != "ok":
        return render(request, 'todo/index.html', {
            'todos' : Todo.objects.all(),
            'error_msg' : exit_code,
        })
    return HttpResponseRedirect(reverse('todo:index'))
