from django.shortcuts import render,redirect
from . models import Task
from . forms import TaskForm
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404
def index(request):
    todo = Task.objects.all()    
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return redirect('index')
    else:
        form=TaskForm()
    context={'todo':todo,'form':form}
    return render(request, 'todo/index.html',context)
def update(request,pk):
    todo=Task.objects.get(id=pk)
    form=TaskForm(instance=todo)
    if request.method=='POST':
       form= TaskForm(request.POST,instance=todo)
       if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'todo/update.html', context)
    
def delete(request,pk):
    try:
        todo=Task.objects.get(id=pk)
        todo.delete()
        return redirect('index')
    except Task.DoesNotExist:
        return HttpResponse("Task not found.", status=404)

def completed(request,pk):
    todo=Task.objects.get(pk=pk)
    todo.completed=True
    todo.save()
    return redirect('index')

def uncompleted(request,pk):
    todo=Task.objects.get(pk=pk)
    todo.completed=False
    todo.save()
    return redirect('index')

