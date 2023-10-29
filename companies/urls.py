from django.urls import path

from .views import (CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView, MyCompanyListAPIView)

app_name = 'companies'

urlpatterns = [
    path('my/', MyCompanyListAPIView.as_view(), name='my_company_list'),
    path('<slug:slug>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy'),
    path('', CompanyListCreateAPIView.as_view(), name='list_create'),
]
