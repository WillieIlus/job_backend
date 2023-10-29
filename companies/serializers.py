from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    get_location = serializers.CharField(source='location')
    get_category = serializers.CharField(source='category')

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('user', 'slug', 'created_at', 'updated_at')
