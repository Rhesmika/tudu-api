from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamSerializer



class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)