from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    get_location = serializers.CharField(source='location', required=False)
    get_category = serializers.CharField(source='category', required=False)
    get_user = serializers.CharField(source='user', required=False)
    logo = Base64ImageField(max_length=None, use_url=True, required=False)
    cover = Base64ImageField(max_length=None, use_url=True, required=False)


    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('user', 'slug', 'created_at', 'updated_at')
