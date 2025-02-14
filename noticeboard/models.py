from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} | written by {self.facilitator}"