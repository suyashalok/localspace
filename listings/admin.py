from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "community", "created_by", "created_at")
    search_fields = ("title", "community__name")
