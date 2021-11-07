from urllib.parse import urlparse

from rest_framework import serializers

from embiq_app import models


class GithubProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GithubProject
        fields = ("url",)

    def validate_url(self, value):
        parsed_url = urlparse(value)
        if parsed_url.netloc != 'github.com':
            raise serializers.ValidationError("Provide valid github url")
        return value


class GithubProjectResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    updated_at = serializers.DateTimeField()
    stars = serializers.IntegerField()
    organization = serializers.CharField(max_length=128)


class GithubProjectDetailResponseSerializer(serializers.Serializer):
    owner = serializers.CharField(max_length=128)
    date = serializers.DateTimeField()
    message = serializers.CharField()
    url = serializers.URLField()
