from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsCommunityMemberOrReadOnly
from communities.models import Community


class CommunityListingView(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = [IsCommunityMemberOrReadOnly]

    # ⭐ Add these three lines:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_by']           # filter by user
    search_fields = ['title', 'description']    # keyword search
    ordering_fields = ['created_at', 'title']   # ordering

    def get_queryset(self):
        community_id = self.kwargs['community_id']
        return Listing.objects.filter(community_id=community_id)

    def perform_create(self, serializer):
        community = Community.objects.get(id=self.kwargs['community_id'])
        serializer.save(
            created_by=self.request.user.userprofile,
            community=community
        )
