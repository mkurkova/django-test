from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bugreports',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='bugreports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'B работе'),
        ('Completed', 'Завершено')
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    PRIORITY_CHOICES = [
        (1, 'Critical'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low'),
        (5, 'Min')
    ]
    priority = models.PositiveIntegerField(
        choices=PRIORITY_CHOICES,
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('Rewiew','Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected' ,'Отклонено'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Рассмотрение',
    )
    PRIORITY_CHOICES = [
        (1, 'Critical'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low'),
        (5, 'Min')
    ]
    priority = models.PositiveIntegerField(
        choices=PRIORITY_CHOICES,
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title