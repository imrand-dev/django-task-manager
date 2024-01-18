from rest_framework import serializers

from tasks.models import TaskPhoto


class TaskPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPhoto 
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "task",
            "photo"
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        photo = validated_data.get("photo")
        task = validated_data.get("task")

        return TaskPhoto.objects.create(created_by=user, task=task, photo=photo)