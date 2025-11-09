from django.db import models
from users.models import UserProfile
from communities.models import Community

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='listings')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.community.name})"
