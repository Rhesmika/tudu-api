from rest_framework import serializers
from boards.models import Board


class BoardSerializer(serializers.ModelSerializer):
    tasks_count = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Board
        fields = [
            "id",
            "created_at",
            "name",
            "owner",
            "is_owner",
            "tasks_count",
        ]
