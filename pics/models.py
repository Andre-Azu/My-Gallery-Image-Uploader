from django.db import models

# Create your models here.
class image(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    picture = models.ImageField(upload_to = 'image/')

    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

