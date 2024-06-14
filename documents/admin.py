from django.contrib import admin
from .models import Document, MetadataField, DocumentMetadata

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'version', 'created_by', 'uploaded_file')

@admin.register(MetadataField)
class MetadataFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_type')

@admin.register(DocumentMetadata)
class DocumentMetadataAdmin(admin.ModelAdmin):
    list_display = ('document', 'field', 'value')
