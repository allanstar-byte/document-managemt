from django.urls import path
from .views import DocumentListCreate, DocumentDetail, MetadataFieldListCreate, MetadataFieldDetail, DocumentMetadataListCreate, DocumentMetadataDetail

urlpatterns = [
    path('documents/', DocumentListCreate.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document-detail'),
    path('metadata-fields/', MetadataFieldListCreate.as_view(), name='metadata-field-list-create'),
    path('metadata-fields/<int:pk>/', MetadataFieldDetail.as_view(), name='metadata-field-detail'),
    path('document-metadata/', DocumentMetadataListCreate.as_view(), name='document-metadata-list-create'),
    path('document-metadata/<int:pk>/', DocumentMetadataDetail.as_view(), name='document-metadata-detail'),
]
