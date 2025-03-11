from django.shortcuts import render, redirect
from .models import Task 
# Create your views here.

def index(request):
    if request.method == "POST":        
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect("index")
    tasks = Task.objects.all()
    return render(request,"todos/index.html", {"tasks":tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("index")