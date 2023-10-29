from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('companies/', include(('companies.urls', 'companies'), namespace='companies')),
    path('categories/', include(('categories.urls', 'categories'), namespace='categories')),
    path('locations/', include(('locations.urls', 'locations'), namespace='locations')),
    path('jobs/', include(('jobs.urls', 'jobs'), namespace='jobs')),
]
