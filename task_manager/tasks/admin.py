from django.contrib import admin

from django.utils.html import format_html

from tasks.models import Task, TaskPhoto 


@admin.register(TaskPhoto)
class TaskPhotoAdmin(admin.ModelAdmin):
    list_display = ["uid", "task_name", "display_image"]
    list_per_page = 15
    list_select_related = ["task",]

    def display_image(self, obj):
        return format_html('<img src="{}" width="75" height="90" />', obj.photo.url)

    display_image.short_description = 'Task_image'

    def task_name(self, obj):
        return obj.task.title


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["uid", "title", "priority", "created_at", "due_date", "is_completed"]
    search_fields = ["title",]
    list_editable = ["due_date",]
    list_per_page = 15
    list_filter = ["created_at", "due_date", "is_completed", "priority"]


