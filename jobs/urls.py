from django.urls import path
from .views import JobList, JobDetail, JobApplicationList, JobApplicationDetail, ImpressionList, ImpressionDetail, ClickList, ClickDetail

app_name = 'jobs'

urlpatterns = [
    path('apply/<slug:slug>/', JobApplicationDetail.as_view(), name='job_application_detail'),
    path('impressions/<slug:slug>/', ImpressionDetail.as_view(), name='impression_detail'),
    path('clicks/<slug:slug>/', ClickDetail.as_view(), name='click_detail'),
    path('clicks/', ClickList.as_view(), name='click_list'),
    path('impressions/', ImpressionList.as_view(), name='impression_list'),
    path('apply/', JobApplicationList.as_view(), name='job_application'),
    path('<slug:slug>/', JobDetail.as_view(), name='job_detail'),
    path('', JobList.as_view(), name='job_list'),
]


