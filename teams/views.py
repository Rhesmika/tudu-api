from rest_framework import permissions, generics
from .models import Team
from .serializers import TeamSerializer
from tudu_api.permissions import IsOwnerOrReadOnly


class TeamList(generics.ListCreateAPIView):
    """
    Lists eteams or create a team if logged in
    The perform_create method associates the team with the logged in user.
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(serializer.data)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a team and edit or delete it if you own it.
    """
    serializer_class = TeamSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Team.objects.all()
