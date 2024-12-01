from django.db import models

class Star(models.Model):
    name = models.CharField(max_length=100)
    constellation = models.CharField(max_length=100)
    magnitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Telescope(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
