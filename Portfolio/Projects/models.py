from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)

class Project(models.Model):
    def __str__(self):
        return self.project_name + ': ' + self.project_desc + '\n'
    
    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=2000)
    project_image = models.ImageField(default='project_pictures/genericproject.jpg', upload_to='project_pictures/')
    project_url = models.URLField(max_length=400, null=True, blank=True)
    project_video = EmbedVideoField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)