from django.urls import path

from tasks.views import TaskListView, TaskDetailView, TaskDeleteView, TaskUpdateView, TaskCreateView, add_photo_to_task

urlpatterns = [
    path("/add", TaskCreateView.as_view(), name='task_create'),
    path("/<slug:task_slug>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("/<slug:task_slug>/update", TaskUpdateView.as_view(), name="task_update"),
    path("/<slug:task_slug>/photo", add_photo_to_task, name="add_task_photo"),
    path("/<slug:task_slug>", TaskDetailView.as_view(), name="task_detail"),
    path("", TaskListView.as_view(), name='task_lists'),
]