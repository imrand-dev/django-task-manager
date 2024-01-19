from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from restapi.rest.serializers.photos import TaskPhotoSerializer

from tasks.models import TaskPhoto


@extend_schema(tags=["tasks"])
class PrivatePhotoView(ListCreateAPIView):
    serializer_class = TaskPhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return TaskPhoto.objects.filter(created_by=user)


@extend_schema(tags=["tasks"])
class PrivatePhotoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskPhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        photo_uid = self.kwargs.get("photo_uid", None)

        return get_object_or_404(TaskPhoto, uid=photo_uid, created_by=user)