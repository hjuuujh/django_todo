from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from todos.models import Todo
from django.urls import reverse

# Create your views here.

def index(request):
    todo_list = Todo.objects.all().order_by('-pub_date')
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, 'todos/detail.html',{'todo':todo})
    
def insert(request):
    # todo = get_object_or_404(Question, pk=question_id)
    return render(request, 'todos/insert.html')

def db_insert(request):
    # try:
    todo = Todo()
    todo.title = request.POST.get('title')
    todo.contents = request.POST.get('contents')
    todo.pub_date = request.POST.get('date')

    if(not todo.title or not todo.contents):
        context =  {'todo': todo, 'error_message': "빈칸 불가능 / 저장 안됨",}
        return render(request, 'todos/notnull.html',context)
    todo.save()
    return HttpResponseRedirect(reverse('index', args=()))

def delete(request, id):
    try:
        selected_todo = get_object_or_404(Todo, pk=id)
    except (KeyError, Todo.DoesNotExist):
        context =  {'todo': todo, 'error_message': "Error",}
        return render(request, 'todos/detail.html',context)
    else:
        selected_todo.delete()
        return HttpResponseRedirect(reverse('index', args=()))

def update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {'id': todo.id}
    return render(request, 'todos/update.html',context)

def db_update(request, id):
    try:
        todo = get_object_or_404(Todo, pk=id)
    except (KeyError, Todo.DoesNotExist):
        context =  {'todo': todo, 'error_message': "Error",}
        return render(request, 'todos/detail.html',context)
    else:
        todo.id = id
        todo.title = request.POST.get('title')
        todo.contents = request.POST.get('contents')
        todo.pub_date = request.POST.get('date')
        todo.save()
        return HttpResponseRedirect(reverse('index', args=()))