from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from task_manager.utils import get_user_tasks  # Import the utility function

@login_required
def home(request):
    if request.method == 'POST':
        fm = TaskForm(request.POST)
        if fm.is_valid():
            task = fm.save(commit=False)
            task.user = request.user  # Associate the task with the logged-in user
            task.save()
            fm = TaskForm()
    else:
        fm = TaskForm()

    # Use the cache function to get tasks before querying the database
    pending_tasks = get_user_tasks(request.user).filter(status='Pending')
    completed_tasks = get_user_tasks(request.user).filter(status='Completed')
    
    return render(request, 'home.html', {
        'form': fm,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    })

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def delete_data(request, id):
    # Fetch the task only if it belongs to the logged-in user
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect('/')

@login_required
def update_data(request, id):
    # Fetch the task only if it belongs to the logged-in user
    task = get_object_or_404(Task, pk=id, user=request.user)

    if request.method == 'POST':
        fm = TaskForm(request.POST, instance=task)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = TaskForm(instance=task)

    return render(request, 'update.html', {'form': fm, 'task': task})
