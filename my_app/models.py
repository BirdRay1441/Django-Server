from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Methodological_materials(models.Model):
    CHOICES = (
        ('L','Lection'),
        ('E','Exam'),
        ('O','Other'),
    )
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to='files/materials')
    data = models.DateField()
    type = models.CharField(max_length = 255, choices = CHOICES)

    def __str__(self):
        return self.title
