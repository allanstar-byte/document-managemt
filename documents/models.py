from django.db import models
from django.contrib.auth.models import User

class MetadataField(models.Model):
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)  # e.g., text, date, number

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class DocumentMetadata(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='metadata')
    field = models.ForeignKey(MetadataField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.document.title} - {self.field.name}: {self.value}'
