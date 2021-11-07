from django.urls import path
from django.conf.urls import include, url

from allauth.socialaccount.providers.github import views as github_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from embiq_app.auth.socials import github
from embiq_app import views

schema_view = get_schema_view(
   openapi.Info(
      title="Embiq task",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('auth/github/', github.GitHubLogin.as_view(), name='github_login'),
   path('auth/github/callback', github.GitHubCallback.as_view(), name='github_callback'),
   path('github/projects', views.GithubProjectView.as_view()),
   path('github/project/<str:name>', views.GithubProjectDetailView.as_view()),
   path('auth/github/token/', github_views.oauth2_login, name='github_token'),
   url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]