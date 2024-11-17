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
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model"""
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
