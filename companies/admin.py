from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'user__username')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at', '-updated_at', 'name')


admin.site.register(Company, CompanyAdmin)
