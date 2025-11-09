from django.urls import path
from .views import UserProfileListCreateView
from .views import RegisterView

urlpatterns = [
    path('', UserProfileListCreateView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
]
