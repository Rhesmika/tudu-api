from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Member
from .serializers import MemberSerializer


class MemberList(APIView):
    serializer_class = MemberSerializer

    
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(
            members, many=True, context={'request': request}
        )
        return Response(serializer.data)
