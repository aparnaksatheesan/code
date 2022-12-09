from django.db import models


# Create your models here.

class Aircraft(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()

    def __str__(self):
        return self.name
