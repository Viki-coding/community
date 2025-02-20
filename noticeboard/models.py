from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import datetime

class CommunityUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    is_facilitator = models.BooleanField(default=False)

def __str__(self):
    return self.user.username

class Location(models.Model):
    LOCATION_CHOICES = [
        ('Main Hall', 'Main Hall'),
        ('Astroturf', 'Astroturf'),
        ('Kitchen', 'Kitchen'),
        ('Meeting Room', 'Meeting Room'),
        ('Pitch', 'Pitch'),
        ('Mezzanine', 'Mezzanine'),
    ]

    name = models.CharField(max_length=50, choices=LOCATION_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('5-Aside Soccer', '5-Aside Soccer'),
        ('GAA', 'GAA'),
        ('St. Olivers Ladies', 'St. Olivers Ladies'),
        ('St. Olivers', 'St. Olivers'),
        ('Finish Valley Athletics', 'Finish Valley Athletics'),
        ('Community Centre', 'Community Centre'),
        ('Yoga', 'Yoga'),
        ('Parent & Toddler Group', 'Parent & Toddler Group'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other')
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    facilitator = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    bookable_event = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField(default=0)
    booking_deadline = models.DateTimeField(blank=True, null=True)

    # If the event is name will create a slug, that slug will be unique to avoic conflicts
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            count = 1
            while Event.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{count}"
                count += 1
            self.slug = unique_slug
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} | written by {self.facilitator}"

    # Booking Model
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CommunityUser, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('event', 'user')

def clean(self):
    if self.event.booking_deadline and self.event.booking_deadline < datetime.now():
        raise ValidationError("Booking deadline has passed.")
    if self.event.capacity <= Booking.objects.filter(event=self.event).count():
        raise ValidationError("Event capacity reached.")
        


    def __str__(self):
        return f"{self.user.user.username} booked {self.event.title}"

# Assign users to groups (Facilitator or Community User)
def assign_user_to_group(user, group_name):
    group, _ = Group.objects.get_or_create(name=group_name)
    if not user.groups.filter(name=group_name).exists():
        user.groups.add(group)