from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import TodoItem


def todoView(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'index.html',
                  {'all_items': all_todo})


def create_todo(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        data = request.POST.get('data')
        todo_obj = TodoItem.objects.create(content=content, data=data)
        return redirect("index")
    return render(request, 'create.html')


def update_data(request, id):
    todo_update = TodoItem.objects.get(id=id)
    if request.method == 'POST':
        content = request.POST.get("content")
        data = request.POST.get('data')
        todo_update.content = content
        todo_update.data = data
        todo_update.save()
        return redirect('index')
    return render(request, 'update.html')


def delete_data(request, id):
    if request.method == 'POST':
        todo = TodoItem.objects.get(id=id)
        todo.delete()
        return redirect('index')
    return render(request, 'delete.html')
