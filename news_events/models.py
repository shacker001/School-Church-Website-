from django.db import models
from cloudinary.models import CloudinaryField


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image_news = CloudinaryField('image', blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="News"

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # image = CloudinaryField('image', blank=True, null=True)
    event_date = models.DateField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
