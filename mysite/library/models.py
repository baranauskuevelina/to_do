from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    task_text = models.CharField(max_length=200, verbose_name='Task text', help_text='Enter the task description')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='tasks')
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Creation datetime')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='LOW', verbose_name='Priority')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO', verbose_name='Status')
    due_date = models.DateField(null=True, blank=True, verbose_name='Due date')

    def __str__(self):
        return self.task_text

    def mark_as_done(self):
        self.status = 'DONE'
        self.save()

    def time_elapsed(self):
        now = timezone.now()
        return now - self.creation_datetime

    @staticmethod
    def get_high_priority_tasks():
        return Task.objects.filter(priority='HIGH')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['task_text']
