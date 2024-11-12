from django.shortcuts import render
from django.http import HttpResponse
from . models import List
from . forms import CreateList
# Create your views here.

def home(request):
    return render(request,'main/home.html')

def task(request,id):
    tasks=List.objects.get(id=id)
    context={'name':tasks.todolist,
             'task':tasks.text}
    return render(request,'main/todo_list.html',context)

def list_tasks(request):
    tasks=List.objects.all()
    return render(request,'main/task_list.html',{'tasks':tasks})

def create_task(request):
    forms=CreateList()
    return render(request,"main/createlist.html",{"forms":forms})