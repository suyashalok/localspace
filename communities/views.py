from rest_framework import generics, permissions
from .models import Community
from .serializers import CommunitySerializer
from .permissions import IsOwnerOrReadOnly

class CommunityListCreateView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        community = serializer.save(created_by=self.request.user.userprofile)
        community.members.add(self.request.user.userprofile)



class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsOwnerOrReadOnly]
