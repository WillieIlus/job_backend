from rest_framework import serializers

from .models import  Job, JobApplication, Impression, Click


class JobSerializer(serializers.ModelSerializer):
    timesince = serializers.SerializerMethodField(required=False)
    get_user = serializers.CharField(source='user', required=False)
    get_company = serializers.CharField(source='company', required=False)
    get_location = serializers.CharField(source='location', required=False)
    get_category = serializers.CharField(source='category', required=False)
    get_job_type = serializers.CharField(source='job_type', required=False)
    get_created_at = serializers.DateTimeField(source='created_at', required=False)
    days_left = serializers.SerializerMethodField(required=False)
    plan_title = serializers.ReadOnlyField(source='plan.title')
    # expired = serializers.SerializerMethodField(required=False)
    # price = serializers.SerializerMethodField(required=False)
    views_count = serializers.IntegerField(read_only=True)
    click_count = serializers.IntegerField(read_only=True)
    # expires_soon = serializers.SerializerMethodField(required=False)
    # time_since = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active', 'slug')

    def get_timesince(self, obj):
        return obj.timesince()

    def get_days_left(self, obj):
        return obj.days_left()


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ('id', 'job', 'user', 'resume', 'cover_letter', 'is_active', 'created_at')
        read_only_fields = ('created_at', 'is_active')

class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impression
        fields = ('id', 'job', 'source_ip', 'session_id', 'created_at')
        read_only_fields = ('created_at',)

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ('id', 'job', 'source_ip', 'session_id', 'created_at')
        read_only_fields = ('created_at',)
