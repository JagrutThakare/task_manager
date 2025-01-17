from celery import shared_task
from tasks.models import Task
from django.utils.timezone import now

@shared_task
def activate_task(task_id):
    print("Task Started")
    try:
        print("Task Executing")
        task = Task.objects.get(id=task_id)
        task.status = 'Pending'  
        task.save()
    except Task.DoesNotExist:
        pass

    print("Task Ended")