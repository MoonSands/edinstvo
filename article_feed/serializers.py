from rest_framework import serializers
from .models import *
from django.conf import settings
import json

#class CategorySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = postCategory
#        fields = '__all__'

class PostFileUpload(serializers.ModelSerializer):
    class Meta:
        model = postContentFilesUpload
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    #category = serializers.PrimaryKeyRelatedField(many=False, queryset=postCategory.objects.all())

    class Meta:
        model = post
        fields = '__all__'   
        
class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = docs
        fields = '__all__'

class ReportGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = reportsGroup
        fields = '__all__'
    
class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reports
        fields = ['id', 'name', 'date', 'file', 'group']

        
        
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataFromForms
        fields = '__all__'