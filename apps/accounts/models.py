from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.market.models import Market
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    markets = models.ManyToManyField(Market, related_name='profiles', blank=True, null=True)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='No bio yet', blank=True, null=True)

    def __str__(self):
        return self.user.username

