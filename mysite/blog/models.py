from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/articles/category/{self.id}/'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[self.created_at.year,
                                            f"{self.created_at.month:02}",
                                            f"{self.created_at.day:02}",
                                            self.slug])


