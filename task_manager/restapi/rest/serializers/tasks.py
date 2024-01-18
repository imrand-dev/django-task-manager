from django.utils import timezone

from rest_framework import serializers

from restapi.rest.serializers.photos import TaskPhotoSerializer

from tasks.models import Task, TaskPhoto


class TaskSerializer(serializers.ModelSerializer):
    task_photos =  TaskPhotoSerializer(many=True, read_only=True)
    uploaded_photos = serializers.ListField(
        child=serializers.ImageField(
        allow_empty_file=False, 
        use_url=False),
        write_only=True
    )

    class Meta:
        model = Task 
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "title",
            "description",
            "due_date",
            "priority",
            "slug",
            "is_completed",
            "task_photos",
            "uploaded_photos",
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
            "slug",
        ]

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        uploaded_photos = validated_data.pop("uploaded_photos")
        task = Task.objects.create(created_by=user, **validated_data)

        for photo in uploaded_photos:
            TaskPhoto.objects.create(created_by=user, task=task, photo=photo)

        return task