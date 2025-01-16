import redis
import json
import pickle
from django.core.cache import cache
from tasks.models import Task

def get_user_tasks(user):
    cache_key = f"user_tasks_{user.id}"
    tasks = cache.get(cache_key)

    r = redis.Redis(host='localhost', port=6379, db=1)  # Adjust host and port as needed
    
    if tasks is None:
        tasks = list(Task.objects.filter(user=user).values())  # Convert queryset to list of dicts (easier to cache)
        # Cache the tasks in JSON format
        cache.set(cache_key, pickle.dumps(tasks), timeout=60*60)  # Cache for 1 Hour (using pickle for more complex data)
        print("=========================================================Data Cached=========================================================")
    else:
        print("=========================================================Data Fetched from Cache=========================================================")

    # Get all keys that match the pattern (tasks keys might start with 'user_tasks')
    keys = r.keys('*')
    print(keys)
    print("=========================================================KEYS=========================================================")
    
    # Print tasks for each key
    for key in keys:
        pickled_data = r.get(key)
        if pickled_data:
            try:
                deserialized_data = pickle.loads(pickled_data)  # Deserialize using pickle
                
                for task in deserialized_data : 
                    print("task", task.id)
                    print("\ttitle : ", task.title,"\n\tdescription : ", task.description,"\n\tstatus : ", task.status)
                    print()

            except Exception as e:
                print(f"Error deserializing data for key {key.decode('utf-8')}: {e}")
            print()
        else:
            print(f"No tasks found for key {key.decode('utf-8')}")
    print("=========================================================KEYS=========================================================")

    # Now the tasks are deserialized (either from cache or the DB)
    return tasks
