from django.db import models

class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
