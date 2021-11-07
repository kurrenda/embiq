import requests
import json
from urllib.parse import urlparse

from rest_framework.exceptions import NotFound
from allauth.socialaccount.models import SocialToken


def get_url_path(url):
    url = urlparse(url)
    path = "/".join(url.path.strip("/").split("/")[0:2])
    return path


def get_access_token(request):
    access_token = SocialToken.objects.get(
            account__user=request.user,
            account__provider='github'
    )
    return access_token


def get_repository(url, access_token):
    path = get_url_path(url)

    r = requests.get(
        f'https://api.github.com/repos/{path}',
        headers={
            "Authorization": f"Token {access_token.token}"
        }
    )

    if r.status_code != 200:
        raise NotFound("Error 404, project not found")

    return r.json()


def set_subscription(url, access_token):
    path = get_url_path(url)

    r = requests.put(
        f'https://api.github.com/repos/{path}/subscription',
        data=json.dumps({"subscribed": True}),
        headers={
            "Authorization": f"Token {access_token.token}"
        }
    )

    if r.status_code != 200:
        raise NotFound("Error 404, project not found")

    return r.json()


def get_subscribed(access_token):
    url = 'https://api.github.com/user/subscriptions'
    data = []
    page = 1
    r = requests.get(
        f'{url}?page={page}&per_page=100',
        headers={
            "Authorization": f"Token {access_token.token}"
        }
    )

    data.extend(r.json())
    is_data = True

    while is_data:
        page += 1
        r = requests.get(
            f'{url}?page={page}&per_page=100',
            headers={
                "Authorization": f"Token {access_token.token}"
            }
        )
        if r.json():
            data.extend(r.json())
        else:
            is_data = False

    return data


def get_watched(queryset, subscribed_projects, access_token):
    results = []
    for project in queryset:
        project_id = project.github_project_id
        if not any(sub['id'] == project_id for sub in subscribed_projects):
            try:
                repository = get_repository(project.url, access_token)
                data = {
                        "name": repository['name'],
                        "updated_at": repository['updated_at'],
                        "stars": repository['stargazers_count']
                }
                if repository['owner']['type'] == "Organization":
                    data['organization'] = repository['owner']['login']
                else:
                    data['organization'] = ''

                set_subscription(project.url, access_token)
                results.append(data)
            except NotFound:
                continue
        else:
            for sub_proj in subscribed_projects:
                if sub_proj['id'] == project_id:
                    data = {
                        "name": sub_proj['name'],
                        "updated_at": sub_proj['updated_at'],
                        "stars": sub_proj['stargazers_count']
                    }
                    if sub_proj['owner']['type'] == "Organization":
                        data['organization'] = sub_proj['owner']['login']
                    else:
                        data['organization'] = ''
                    results.append(data)
    return results


def get_last_commit(url, access_token):
    path = get_url_path(url)
    NEWEST_ELEMENT = 0

    r = requests.get(
        f'https://api.github.com/repos/{path}/commits',
        headers={
            "Authorization": f"Token {access_token.token}"
        }
    )

    if r.status_code != 200:
        raise NotFound("Error 404, Any commit not found")

    commit = r.json()[NEWEST_ELEMENT]
    data = {
            "owner": commit['commit']['author']['name'],
            "date": commit['commit']['author']['date'],
            "message": commit['commit']['message'],
            "url":  f'https://api.github.com/repos/{path}/zipball/'
    }

    return data
