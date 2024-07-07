from django.db import models

class History(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class MissionStatement(models.Model):
    statement = models.TextField()

    def __str__(self):
        return "Mission Statement"
