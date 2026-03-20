from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):

    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='driver')

    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"