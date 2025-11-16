from django.urls import path
from .views import CommunityListCreateView, CommunityDetailView
from listings.views import CommunityListingView

urlpatterns = [
    path('', CommunityListCreateView.as_view(), name='community-list'),
    path('<int:pk>/', CommunityDetailView.as_view(), name='community-detail'),

    #Nested route for listings inside a community
    path('<int:community_id>/listings/', CommunityListingView.as_view(), name='community-listings'),
]
