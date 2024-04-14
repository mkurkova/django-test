from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'B работе'),
        ('Completed', 'Завершено')
    ]
    project = models.ForeignKey(
        Project,
        related_name='tasks',
        on_delete=models.CASCADE                #показывает, что при удалении все данные будут удалены
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    #дата и время создания задачи
    updated_at = models.DateTimeField(auto_now=True)    #автоматически обновляет дату и время при обновлении задачи
    assignee = models.ForeignKey( 
        User,
        related_name='tasks',       #позволяет обращаться к задаче
        on_delete=models.SET_NULL,  #указывает, что если поле удаляется, поле assignee обращается в нуль
        null=True,
        blank=True              #разрешает быть полю пустым
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,     #позволяет установить ограниченный набор опций
        default='New',          #устанавливает значение по умолчанию для статуса
    )


