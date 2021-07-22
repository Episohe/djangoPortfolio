from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=80)
    stack = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    url = models.URLField(max_length=200)
    img_path = models.CharField(max_length=255)

def __str__(self):
    return self.title
