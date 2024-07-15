from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

from . import models
from .models import Task

def closed_tasks_last_month():
    one_month_ago = timezone.now() - timedelta(days=30)
    return Task.objects.filter(completed=True, updated_at__gte=one_month_ago)

def tasks_with_status_and_type():
    return Task.objects.filter(
        Q(status__in=['todo', 'done']) & Q(task_type__in=['bug', 'feature'])
    )

def open_tasks_with_bug_in_name():
    return Task.objects.filter(
        ~Q(completed=True),
        Q(title__icontains='bug') | Q(task_type='bug')
    )

def task_fields_only():
    return Task.objects.values('id', 'title', 'task_type', 'status')

def tasks_with_equal_description():
    return Task.objects.filter(description=models.F('title'))

def count_tasks_by_type():
    return Task.objects.values('task_type').annotate(count=models.Count('id'))
