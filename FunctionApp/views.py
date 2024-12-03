from django.shortcuts import render,redirect
from django.http import HttpResponse
from FunctionApp.models import Task
import datetime


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        # due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
        
        # Create a new Task object
        if title and status and due_date:
            new_task = Task(title=title, status=status, due_date=due_date)
            new_task.save()
            return redirect('index') # Redirect to the task list page after adding the task

    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'index.html', {'tasks': tasks})

# def task_list(request):
#     tasks = Task.objects.all()  # Retrieve all tasks from the database
#     return render(request, 'index.html', {'tasks': tasks})


# def add_task(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         status = request.POST.get('status')
#         due_date = request.POST.get('due_date')
#         # due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
        
#         # Create a new Task object
#         if title and status and due_date:
#             new_task = Task(title=title, status=status, due_date=due_date)
#             new_task.save()
#             return redirect('index') # Redirect to the task list page after adding the task

            
#     return render(request, 'index.html',{})

def delete(request,name):
     if request.method== 'POST':
        getBack=Task.objects.get(title=name)
        getBack.delete()
        return redirect('index')

def update(request,name):
    if request.method=='POST':
        getBack=Task.objects.get(title=name)
        getBack.status='completed'
        getBack.save()
        return redirect('index')