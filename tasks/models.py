from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Scheduled', 'Scheduled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    start_of_week = models.DateTimeField()
    end_of_week = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Report for {self.user.username} ({self.start_of_week} - {self.end_of_week})"
