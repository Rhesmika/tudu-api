from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id', 'owner', 'created_at', 'image', 'is_owner'
        ]