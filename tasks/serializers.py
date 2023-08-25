from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User
from boards.models import Board


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "board",
            "created_at",
            "title",
            "description",
            "attachment",
            "duedate",
            "priority",
            "status",
            "is_owner",
        ]
