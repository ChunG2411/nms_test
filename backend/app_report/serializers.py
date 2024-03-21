from rest_framework import serializers
from .models import *


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class IndustryReportSerializer(serializers.ModelSerializer):
    industry = serializers.SerializerMethodField()

    class Meta:
        model = IndustryReport
        fields = '__all__'
    
    def get_industry(self, obj):
        return IndustrySerializer(obj.industry).data


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandReportSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()

    class Meta:
        model = BrandReport
        fields = '__all__'

    def get_brand(self, obj):
        return BrandSerializer(obj.brand).data