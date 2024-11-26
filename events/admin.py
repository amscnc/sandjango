from django.contrib import admin
from .models import Event, Venue

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'has_venue', 'start_time', 'end_time')

    def has_venue(self, obj):
        return obj.venue is not None
    has_venue.boolean = True  # Displays as a boolean icon in admin
    has_venue.short_description = 'Has Venue'

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'street_address', 'city', 'state', 'zip_code', 'country', 'description')