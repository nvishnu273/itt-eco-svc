# from django.db import models
from django.contrib.gis.db import models
# from django.contrib.auth.models import User

# Create your models here.
class OrganizationType(models.Model):
    """Type of organizer lookup."""
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, help_text="The type of the organization.")   
    def __str__(self):
        return self.title

class Organizer(models.Model):
    """A festival of any kind that is celebrated."""
    title = models.CharField(max_length=200, help_text="The name of the organizer.")
    description = models.TextField()
    organizer = models.CharField(max_length=200, help_text="The organizer of the event. Could be religeous institution, art institutions or any other.")
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=6)
    poly = models.PolygonField()
    website = models.URLField(help_text="The Event's associated website.")
    # email = models.EmailField(help_text="The email address.")
    def __str__(self):
        return self.title

class Event(models.Model):
    """A festival of any kind that is celebrated."""
    title = models.CharField(max_length=200, help_text="The name of the event.")
    description = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, help_text="The organizer of the event. Could be religeous institution, art institutions or any other.")    
    location = models.CharField(max_length=200)
    website = models.URLField(help_text="The Event's associated website.")
    def __str__(self):
        return self.title

