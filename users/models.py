from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """Extends the default Django's User model"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.TextField(max_length=10, blank=True)
    profile_picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
