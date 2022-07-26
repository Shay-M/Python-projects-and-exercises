from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)  # ! max_length = required
    description = models.TextField(blank=True, null=True)  # blank is required
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    # if we add new Field : null=True, default=True
    featured = models.BooleanField(default=False)
