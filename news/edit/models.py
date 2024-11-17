from django.db import models

class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class News(models.Model):
    """News model
    """
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to="images/")
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
