from .models import Job
from locations.models import Location
from categories.models import Category
from django_filters import rest_framework as filters


class JobFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    location = filters.ModelChoiceFilter(queryset=Location.objects.all())
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    job_type = filters.ChoiceFilter(choices=Job.JOB_TYPE_CHOICES)
    openings = filters.NumberFilter(field_name='openings', lookup_expr='gte')

    class Meta:
        model = Job
        fields = {
            'title',
            'location',
            'category',
            'salary',
            'job_type',
            'openings'
        }

