from django.db import IntegrityError
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

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
