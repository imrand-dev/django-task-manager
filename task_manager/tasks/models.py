from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone

from autoslug import AutoSlugField

from common.base_model import BaseModelWithUID
from tasks.choices import TaskPriority

from account.models import User


class Task(BaseModelWithUID):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        unique_with="title",
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=7,
        choices=TaskPriority.choices,
        default=TaskPriority.LOW
    )
    due_date = models.DateField(default=timezone.now().date() + timezone.timedelta(days=1))
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    def save(self, *args, **kwargs):
        if self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")
        
        super().save(*args, **kwargs)


class TaskPhoto(BaseModelWithUID):
    task = models.ForeignKey(
        to=Task,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="task_photos"
    )
    photo = models.ImageField(upload_to="photos/")
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return str(self.uid)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"