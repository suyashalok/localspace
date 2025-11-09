from django.urls import path
from .views import UserProfileListCreateView

urlpatterns = [
    path('', UserProfileListCreateView.as_view(), name='user-list'),
]
