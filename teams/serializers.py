from rest_framework import serializers
from teams.models import Team
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    members = UserSerializer(many=True)

    task_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Team
        fields = [
            "id",
            "created_at",
            "name",
            "description",
            "image",
            "owner",
            "is_owner",
            "task_count",
            "members",
        ]
