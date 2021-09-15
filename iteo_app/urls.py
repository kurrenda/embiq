from django.urls import path, re_path

from iteo_app import views

urlpatterns = [
    path('upload', views.FileUploadView.as_view())
]