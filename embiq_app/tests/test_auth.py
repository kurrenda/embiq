from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):
    def test_routes_protected(self):
        """Testing if routes are protected from anonymous users"""

        routes_get = [
            '/github/projects',
            '/github/project/embiq'
        ]

        routes_post = [
            '/github/projects'
        ]

        for r in routes_get:
            response_get = self.client.get(r)
            self.assertEqual(response_get.status_code, 401)

        payload = {
            "test": 'test',
        }

        for rp in routes_post:
            response_post = self.client.post(rp, payload)
            self.assertEqual(response_post.status_code, 401)
