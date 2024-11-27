from django.db                      import models
# from django.contrib.gis.db          import models as gis_models
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# def get_coordinates(address):
#     geolocator = Nominatim(user_agent="myapp")
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return location.latitude, location.longitude
#     except GeocoderTimedOut:
#         return None
#     return None

# from django.db import models
# import geocoder

# class YourModel(models.Model):
#     address = models.CharField(max_length=255)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.latitude and not self.longitude:
#             g = geocoder.google(self.address)
#             if g.ok:
#                 self.latitude = g.lat
#                 self.longitude = g.lng
#         super().save(*args, **kwargs)

class Venue(models.Model):
    name                = models.CharField(max_length=255)
    street_address      = models.CharField(max_length=255, blank=False, null=False)
    city                = models.CharField(max_length=100, blank=False, null=False)
    state               = models.CharField(max_length=100, blank=False, null=False)
    zip_code            = models.CharField(max_length=20, blank=False, null=False)
    country             = models.CharField(max_length=100, blank=False, null=False)
    description         = models.TextField(blank=True)
    # cooridinates = gis_models.PointField(geography=True, null=False, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.coordinates and self.street_address and self.city:
    #         address = f"{self.street_address}, {self.city}, {self.state}, {self.country}"
    #         coords = get_coordinates(address)
    #         if coords:
    #             self.coordinates = Point(coords[1], coords[0])  # Note (lon, lat) order
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    name                = models.CharField(max_length=200)
    venue               = models.ForeignKey("Venue", on_delete=models.SET_NULL, null=True, blank=True, related_name="events")
    start_time          = models.DateTimeField(blank=False)
    end_time            = models.DateTimeField(blank=False)
    description         = models.TextField(blank=True)

    def __str__(self):
        return self.name