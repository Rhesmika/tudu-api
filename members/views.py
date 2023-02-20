from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Member
from .serializers import MemberSerializer
from tudu_api.permissions import IsOwnerOrReadOnly, IsAuthenticated


class MemberList(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        return Response(serializer.data)

class MemberDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MemberSerializer

    def get_object(self, pk):
        try:
            member = Member.objects.get(pk=pk)
            self.check_object_permissions(self.request, member)
            return member
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer()(
            member, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )