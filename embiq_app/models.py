from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils.text import slugify 


class GithubProject(models.Model):
    name = models.CharField(max_length=128, blank=True)
    url = models.URLField(max_length=128, unique=True)
    github_project_id = models.PositiveBigIntegerField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GithubProject, self).save(*args, **kwargs)


class GithubUserProject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )
    project = models.ForeignKey(
        GithubProject,
        on_delete=models.CASCADE,
        related_name='project'
    )
