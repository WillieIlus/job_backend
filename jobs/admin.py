from django.contrib import admin

from .models import Job, JobApplication, Impression, Click


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'company', 'location', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'company', 'location', 'is_active')
    search_fields = ('title', 'description', 'requirements', 'company__name', 'location__name')
    list_per_page = 20

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'is_active')
    list_filter = ('job', 'user', 'is_active')
    search_fields = ('job__title', 'user__username')
    list_per_page = 20

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('job', 'source_ip', 'session_id', 'created_at')
    list_filter = ('job', 'source_ip', 'session_id')
    search_fields = ('job__title', 'source_ip', 'session_id')
    list_per_page = 20

class ClickAdmin(admin.ModelAdmin):
    list_display = ('job', 'source_ip', 'session_id', 'created_at')
    list_filter = ('job', 'source_ip', 'session_id')
    search_fields = ('job__title', 'source_ip', 'session_id')
    list_per_page = 20

admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Impression, ImpressionAdmin)
admin.site.register(Click, ClickAdmin)


