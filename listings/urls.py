from django.urls import path
from .views import CommunityListingView

urlpatterns = [
    path('community/<int:community_id>/', CommunityListingView.as_view(), name='community-listings'),
]
