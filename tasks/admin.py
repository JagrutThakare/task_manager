from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'due_date', 'status', 'description')
