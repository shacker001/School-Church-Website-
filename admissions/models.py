from django.db import models

class AdmissionStep(models.Model):
    step_number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step_number}"

class ImportantDate(models.Model):
    event = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.event
