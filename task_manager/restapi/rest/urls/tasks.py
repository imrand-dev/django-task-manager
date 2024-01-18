from django.urls import path 

from restapi.rest.views.tasks import PrivateTaskView, PrivateTaskDetailView

urlpatterns = [
    path("/<uuid:task_uid>", PrivateTaskDetailView.as_view(), name="task-detail"),
    path("", PrivateTaskView.as_view(), name="task-list"),
]