from django.test import TestCase

from embiq_app.serializers import GithubProjectSerializer


class GithubProjectTest(TestCase):
    """ Test module for GithubProject model """

    def test_project_serializer_invalid(self):
        data = {
            'name': 'invalid', 
            'url': 'https://www.example.com/test/test',
            'github_project_id': 11
        }

        serializer = GithubProjectSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)

    def test_project_serializer_valid(self):
        data = {
            'name': 'valid', 
            'url': 'https://github.com/kurrenda/Embiq',
            'github_project_id': 12
        }

        serializer = GithubProjectSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)