from django.db import models
from django.urls import reverse

from django.utils.text import slugify


# Create your Country and Location models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    flag = models.ImageField(upload_to='countries/flags/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    flag = models.ImageField(upload_to='locations/flags/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['-created_at', '-name']

    def __str__(self):
        return self.name

    def get_jobs(self):
        return self.jobs.all()

    def get_active_jobs(self):
        return self.jobs.filter(active=True)

    def get_active_jobs_count(self):
        return self.jobs.filter(active=True).count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location:detail', kwargs={'slug': self.slug})

