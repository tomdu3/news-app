from django.db import models

class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
