from rest_framework import serializers
from boards.models import Board


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    task_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Board
        fields = [
            "id",
            "owner",
            "created_at",
            "name",
            "is_owner",
            "team",
            "task_count",
        ]
