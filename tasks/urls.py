from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
]


from django.shortcuts import render, get_object_or_404
from .models import Task

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})


