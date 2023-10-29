from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_jobs(self):
        return self.jobs.all()

    def get_active_jobs(self):
        return self.jobs.filter(active=True)

    def get_active_jobs_count(self):
        return self.jobs.filter(active=True).count()



