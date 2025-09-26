from django.db import models

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.fullname