from rest_framework import generics, permissions
from .models import Document, DocumentMetadata, MetadataField
from .serializers import DocumentSerializer, MetadataFieldSerializer, DocumentMetadataSerializer

class DocumentListCreate(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class MetadataFieldListCreate(generics.ListCreateAPIView):
    queryset = MetadataField.objects.all()
    serializer_class = MetadataFieldSerializer
    permission_classes = [permissions.IsAuthenticated]

class MetadataFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetadataField.objects.all()
    serializer_class = MetadataFieldSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocumentMetadataListCreate(generics.ListCreateAPIView):
    queryset = DocumentMetadata.objects.all()
    serializer_class = DocumentMetadataSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocumentMetadataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentMetadata.objects.all()
    serializer_class = DocumentMetadataSerializer
    permission_classes = [permissions.IsAuthenticated]
