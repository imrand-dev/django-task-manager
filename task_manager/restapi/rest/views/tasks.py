from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from drf_spectacular.utils import extend_schema

from restapi.rest.serializers.tasks import TaskSerializer

from tasks.models import Task


@extend_schema(tags=["tasks"])
class PrivateTaskView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    parser_class = [MultiPartParser, FormParser]
    # http_method_names = ["get", "post"]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(created_by=user)


@extend_schema(tags=["tasks"])
class PrivateTaskDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    # http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        user = self.request.user
        task_uid = self.kwargs.get("task_uid", None)
        
        return get_object_or_404(Task, uid=task_uid, created_by=user)