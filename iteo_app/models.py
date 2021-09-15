from django.db import models
from django.core.validators import FileExtensionValidator


class File(models.Model):
    file = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )
    columns = models.TextField()
