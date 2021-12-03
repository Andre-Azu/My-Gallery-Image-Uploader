from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    pics_image = models.ImageField(upload_to = 'Image/')

    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

