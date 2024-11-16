from django.db import models
# from cloudinary.models import CloudinaryField

class ChurchProgram(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.author
