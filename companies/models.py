from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

from locations.models import Location
from categories.models import Category

User = settings.AUTH_USER_MODEL

class Company(models.Model):
    name = models.CharField( max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    logo = models.ImageField(upload_to='companies/', verbose_name=_('Logo'), blank=True, null=True)
    cover = models.ImageField(upload_to='companies/', verbose_name=_('Cover'), blank=True, null=True)
    website = models.URLField(verbose_name=_('Website'), blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name=_('Phone'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name=_('Address'), blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='companies')
    category = models.ForeignKey(Category, null=True, blank=True,  on_delete=models.CASCADE, verbose_name=_('Category'), related_name='companies')
    location = models.ForeignKey(Location, null=True, blank=True,  on_delete=models.CASCADE, verbose_name=_('Location'), related_name='companies')

    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ('-created_at','-updated_at','name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companies:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def get_jobs(self):
        return self.jobs.all()

    def get_logo_url(self):
        if self.logo:
            return self.logo.url
        else:
            return '/static/images/default-company-logo.png'
