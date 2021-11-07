
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from embiq_app import serializers
from embiq_app import models
from embiq_app.utils import github_util


class GithubProjectView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GithubProjectSerializer
    queryset = models.GithubProject.objects.all()

    def create(self, request, *args, **kwargs):
        access_token = github_util.get_access_token(request)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = serializer.validated_data['url']
        project_data = github_util.get_repository(url, access_token)

        serializer.save(
            name=project_data['name'],
            github_project_id=project_data['id']
        )
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def list(self, request):
        queryset = self.get_queryset()
        access_token = github_util.get_access_token(request)
        subscribed_projects = github_util.get_subscribed(access_token)

        results = github_util.get_watched(
            queryset, subscribed_projects, access_token)

        serializer = serializers.GithubProjectResponseSerializer(
            results,
            many=True)
        return Response(serializer.data)


class GithubProjectDetailView(generics.RetrieveAPIView):
    queryset = models.GithubProject.objects.all()
    serializer_class = serializers.GithubProjectDetailResponseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'

    def get_object(self):
        access_token = github_util.get_access_token(self.request)
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, slug=slugify(self.kwargs['name']))
        last_commit = github_util.get_last_commit(obj.url, access_token)

        return last_commit
