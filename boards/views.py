from django.db.models import Count
from rest_framework import permissions, generics, filters
from tudu_api.permissions import IsOwnerOrReadOnly
from .models import Board
from .serializers import BoardSerializer


class BoardList(generics.ListCreateAPIView):
    """
    List boards or create a post if logged in
    The perform_create method associates the board with the logged in user.
    """

    serializer_class = BoardSerializer

    queryset = qs.annotate(
        tasks_count=Count("tasks", distinct=True),
    ).order_by("-created_at")

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "name",
        "tasks__title",
    ]
    ordering_fields = [
        "tasks_count",
        "tasks__title",
    ]

    def get_queryset(self):
        qs = Board.objects.filter(
            owner=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a board and edit or delete it if you own it.
    """

    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Board.objects.annotate(
        tasks_count=Count("tasks", distinct=True),
    ).order_by("-created_at")
