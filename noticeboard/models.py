from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    time = models.TimeField()
    endtime = models.TimeField()
    location = models.CharField('Location', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    facilitator = models.ForeignKey('Facilitator', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
