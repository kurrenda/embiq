from rest_framework import serializers

from iteo_app import models


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = "__all__"