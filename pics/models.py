from django.db import models

# Create your models here.
class image(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=400)

