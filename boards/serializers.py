from rest_framework import serializers
from boards.models import Board


class BoardSerializer(serializers.ModelSerializer):
    task_count = serializers.ReadOnlyField()

    class Meta:
        model = Board
        fields = [
            "id",
            "created_at",
            "name",
            "team",
            "task_count",
        ]
