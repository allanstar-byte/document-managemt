from rest_framework import serializers
from .models import Document, MetadataField, DocumentMetadata

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'uploaded_file', 'uploaded_at', 'version', 'created_by')

class MetadataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataField
        fields = ('id', 'name', 'field_type')

class DocumentMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentMetadata
        fields = ('id', 'document', 'field', 'value')
