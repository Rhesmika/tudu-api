from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    team = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Member
        fields = [
            'id', 'created_at',  'owner', 'team', 'status',
        ]