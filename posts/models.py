from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=400)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)
