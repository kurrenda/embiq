
from django.shortcuts import redirect, reverse

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView
from rest_framework.response import Response


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    schema = None

    def get(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.GET)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return Response({'token': str(self.token)})

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('github_callback'))


class GitHubCallback(APIView):
    schema = None

    def get(self, request):
        return redirect(reverse('github_login')+f"?code={request.GET['code']}")
