from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('companies/', include(('companies.urls', 'companies'), namespace='companies')),
    path('categories/', include(('categories.urls', 'categories'), namespace='categories')),
    path('locations/', include(('locations.urls', 'locations'), namespace='locations')),
    path('jobs/', include(('jobs.urls', 'jobs'), namespace='jobs')),
    # path('plans/', include(('plans.urls', 'plans'), namespace='plans')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
