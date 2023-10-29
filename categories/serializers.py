from  rest_framework import serializers

from jobs.models import Job
from jobs.serializers import JobSerializer

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    job_count = serializers.SerializerMethodField()
    jobs = JobSerializer(many=True, read_only=True)

    def get_job_count(self, category):
        return Job.objects.filter(category=category).count()

    class Meta:
        model = Category
        # fields = ['name', 'slug', 'description']
        fields = '__all__'
        read_only_fields = ['slug']
