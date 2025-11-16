from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    community = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'created_by', 'community', 'created_at', 'updated_at']
