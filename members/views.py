from rest_framework import permissions, generics
from tudu_api.permissions import IsOwnerOrReadOnly
from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    """
    List memberships or create a membership if logged in
    The perform_create method associates the membership with the logged in user.
    """
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(serializer.data)


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a membership and edit or delete it if you own it.
    """
    serializer_class = MemberSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Member.objects.all()
