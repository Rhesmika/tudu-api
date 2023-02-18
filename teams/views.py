from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamSerializer
from tudu_api.permissions import IsOwnerOrReadOnly
from django.http import Http404


class TeamList(APIView):
    serializer_class = TeamSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TeamDetail(APIView):
    serializer_class = TeamSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            team = Team.objects.get(pk=pk)
            self.check_object_permissions(self.request, team)
            return team
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(
            team, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        team = self.get_object(pk)
        team.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
