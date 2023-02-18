from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    # members = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='username'
    # )
    is_member = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    def get_is_member(self, obj):
        request = self.context['request']
        return obj.members.filter(username=request.user).exists()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Team
        fields = [
            'id', 'created_at', 'name', 'description', 'image', 'owner', 'is_owner', 'members', 'is_member',
        ]
