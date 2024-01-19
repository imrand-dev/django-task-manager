from django import forms

from tasks.models import Task, TaskPhoto


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
            "priority",
            "is_completed",
        ]


class AddTaskPhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ["photo", "task"]