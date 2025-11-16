from django.db import models
from django.db import models
from users.models import UserProfile

class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='communities_created')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(UserProfile, related_name='communities')

    def __str__(self):
        return self.name

# Create your models here.
