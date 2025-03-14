# Task Management System
---
## Technologies Used:
<div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center;"> 
    <img src="/static/images/python.png" alt="Python" style="width: 160px; height: 70px;"> 
    <img src="/static/images/html.png" alt="HTML" style="width: 80px; height: 70px;"> 
    <img src="/static/images/bootstrap.png" alt="Bootstrap" style="width: 100px; height: 70px;"> 
    <img src="/static/images/pst.png" alt="PostgreSQL" style="width: 70px; height: 70px;"> 
    <img src="/static/images/redis.png" alt="Redis" style="width: 70px; height: 70px;"> 
    <img src="/static/images/celery.png" alt="Celery" style="width: 70px; height: 70px;"> 
</div>

- HTML
- Bootstrap 5
- PostgreSQL
- Redis
- Celery & Celery Beat

## Demo
<video width="640" height="360" controls>
  <source src="static/videos/Project.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Schema
![](/static/images/Schema.png)


## Workflow
![](/static/images/workflow.jpg)


## References

- [Youtube](https://www.youtube.com/watch?v=OPc_oMgjhpM)
- [W3 Schools - Django](https://www.w3schools.com/django/index.php)
- [Medium - How to Build a Simple Task Management System](https://medium.com/@farad.dev/how-to-build-a-simple-task-management-api-with-django-a9d0cd28c85e)

## Performs CRUD Operations

![Project Image](/static/images/project.png)
![Project Image](/static/images/Login.png)
## Sample Http Requests: (USE POSTMAN)


#### 1. Post Request
- create task in database.
- copy this and paste in body.
```bash
{
    "title": "New Task",
    "description": "Details of the new task",
    "status": "COMPLETED",
    "deadline": "2025-01-29"
}
``` 
- select request to post
- in the url type http://127.0.0.1:8000/api/tasks/

#### 2. GET Request
- Fetch task from database.
- select request to post
- in the url type http://127.0.0.1:8000/api/tasks/ or http://127.0.0.1:8000/api/tasks/1/

#### 3. PUT Request
- update task in database.
- change what you want in the body
```bash
{
    "title": "New Task",
    "description": "Details of the new task",
    "status": "PENDING",
    "deadline": "2025-01-29"
}
```
- select request to PUT
- in the url type http://127.0.0.1:8000/api/tasks/1/

#### 4. DELETE Request
- Delete task in database.
- select request to DELETE
- in the url type http://127.0.0.1:8000/api/tasks/1/



# Developer Journey :

### Django Commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```   

### Docker commands to create and use Redis
```bash
docker run --name redis -p 6379:6379 -d redis
docker exec -it redis redis-cli
```

### Celery Commands :

```bash
celery -A task_manager worker --loglevel=info -P solo
celery -A task_manager beat --loglevel=info
celery -A task_manager flower --port=5555
```     
