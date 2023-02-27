from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User




class TaskSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "created_at",
            "title",
            "description",
            "attachment",
            "duedate",
            "priority",
            "status",
            "is_owner",
        ]
