from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from iteo_app import models


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(
        max_length=100,
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )
    columns = serializers.CharField(style={'base_template': 'textarea.html'})
