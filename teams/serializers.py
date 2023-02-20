from rest_framework import serializers
from teams.models import Team
from members.models import Member


class TeamSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    member_count = serializers.ReadOnlyField()
    task_count = serializers.ReadOnlyField()


    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    member_id = serializers.SerializerMethodField()

    def get_member_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            member = Member.objects.filter(
                owner=user, team=obj.id
            ).first()
            return member.id if member else None
        return None

    class Meta:
        model = Team
        fields = [
            'id', 'created_at', 'name', 'description', 'image', 'owner', 'is_owner', 'member_id', 'member_count', 'task_count'
        ]
