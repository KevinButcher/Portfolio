from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    def __str__(self):
        return self.name + ': ' + self.skill_type + '\n'
    
    SKILL_TYPE_CHOICES = [
        ('technical', 'Technical'),
        ('soft', 'Soft'),
    ]

    name = models.CharField(max_length=50)
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE_CHOICES)

class Profile(models.Model):
    def __str__(self):
        return self.user.username
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pictures/profilepic.jpg', upload_to='profile_pictures/', blank=True)
    location = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    skills=models.ManyToManyField(Skill, blank=True)