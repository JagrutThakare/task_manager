from django.core.cache import cache
from tasks.models import Task

def get_user_tasks(user):
    cache_key = f"user_tasks_{user.id}"
    tasks = cache.get(cache_key)
    
    if tasks is None:
        tasks = Task.objects.filter(user=user)  
        print(type(tasks))
        print(tasks)
        cache.set(cache_key, tasks, timeout=60*60) 
        print("=========================================================Data Cached=========================================================")
        print(tasks)
    else:
        print("=========================================================Data Fetched from Cache=========================================================")
        print(tasks)
    return tasks
