from rest_framework import serializers
from .models import *

class PageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageTypeModel
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContentModel
        fields = '__all__'
