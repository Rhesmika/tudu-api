from rest_framework import permissions, generics
from .models import Profile
from .serializers import ProfileSerializer
from tudu_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListCreateAPIView):
    """
    List profiles or create a profile if logged in
    The perform_create method associates the profile with the logged in user.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a profile and edit or delete it if you own it.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
