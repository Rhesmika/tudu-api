from rest_framework import serializers
from teams.models import Team
from members.models import Member


class TeamSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    member_id = serializers.SerializerMethodField()
    # def get_following_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         following = Follower.objects.filter(
    #             owner=user, followed=obj.owner
    #         ).first()
    #         # print(following)
    #         return following.id if following else None
    #     return None


    def get_member_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            member = Member.objects.filter(
                owner=user, team=obj.id
            ).first()
            # print(following)
            return member.id if member else None
        return None



    # members = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='username'
    # )

    # is_member = serializers.SerializerMethodField()

    # def get_is_member(self, obj):
    #     request = self.context['request']
    #     return obj.members.filter(username=request.user).exists()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Team
        fields = [
            'id', 'created_at', 'name', 'description', 'image', 'owner', 'is_owner','member_id'
        ]
