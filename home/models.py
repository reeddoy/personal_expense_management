from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('trial', 'Trial'),
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=50, blank=True, null=True)
    security_code = models.CharField(max_length=50, blank=True, null=True)
    email_notification = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='trial')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, default='profile/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username