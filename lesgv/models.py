from django.db import models

# Create your models here.
from django.urls import reverse


class LgvPage(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)  # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lgv_page", kwargs={"slug": self.slug})
