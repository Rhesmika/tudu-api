from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board
from .serializers import BoardSerializer


class BoardList(APIView):
    serializer_class = BoardSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(
            boards, many=True, context={'request': request}
        )
        return Response(serializer.data)