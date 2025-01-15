# Task Management System
---

## Technologies Used:
- Django (Python Framework)
- HTML
- Bootstrap 5
- PostgreSQL

## Performs CRUD Operations

![Project Image](/static/images/project.png)
![Project Image](/static/images/Login.png)
## Sample Http Requests: (USE POSTMAN)

#### 1. Post Request
- create task in database.
- copy this and paste in body.
> {"title": "New Task","description": "Details of the new task","status": "COMPLETED","deadline": "2025-01-29"}
- select request to post
- in the url type http://127.0.0.1:8000/api/tasks/

#### 2. GET Request
- Fetch task from database.
- select request to post
- in the url type http://127.0.0.1:8000/api/tasks/ or http://127.0.0.1:8000/api/tasks/1/

#### 3. PUT Request
- update task in database.
- change what you want in the body
> {"title": "New Task","description": "Details of the new task","status": "PENDING","deadline": "2025-01-29"}
- select request to PUT
- in the url type http://127.0.0.1:8000/api/tasks/1/

#### 4. DELETE Request
- Delete task in database.
- select request to DELETE
- in the url type http://127.0.0.1:8000/api/tasks/1/


## Schema
![](/static/images/Schema.png)


## Workflow
![](/static/images/workflow.jpg)


## References

- [Youtube](https://www.youtube.com/watch?v=OPc_oMgjhpM)
- [W3 Schools - Django](https://www.w3schools.com/django/index.php)
- [Medium - How to Build a Simple Task Management System](https://medium.com/@farad.dev/how-to-build-a-simple-task-management-api-with-django-a9d0cd28c85e)