from io import BytesIO

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from rest_framework.test import APITestCase

from iteo_app.excel.calculator import ExcelCalc


class ExcelCalcTestCase(APITestCase):
    def setUp(self):
        self.result_values = [
            {'column': 'CURRENT USD', 'sum': 18306.05, 'avg': 27.28},
            {'column': ' CURRENT CAD', 'sum': 22406.74, 'avg': 33.39},
            {'column': 'THIS IS THE  PRICE NEW PRICE IN US DOLLARS', 'sum': 19191.05, 'avg': 28.60},
            {'column': 'THIS IS THE  PRICE NEW PRICE IN CANADIAN DOLLARS', 'sum': 23454.60, 'avg': 34.95},
            {'column': 'USD', 'sum': 2047.80, 'avg': 32.00},
            {'column': 'CAD', 'sum': 2497.95, 'avg': 39.03},
            {'column': 'USD', 'sum': 2200.80, 'avg': 34.39},
            {'column': 'CAD', 'sum': 2660.20, 'avg': 41.57}
        ]

    def test_computing_avg_sum_values(self):
        """Testing if column avg and sum values are equal"""
        
        file = File(open(
            "iteo_app/tests/example_data/us trade price changes2011_nofc.xlsx",
            "rb"
        ))

        file_name = "us trade price changes2011_nofc.xlsx"

        upload_file = SimpleUploadedFile(
            file_name,
            file.read(),
            content_type='multipart/form-data'
        )

        columns = (
            ' CURRENT USD,'
            ' CURRENT CAD,'
            'THIS IS THE  PRICE NEW PRICE IN US DOLLARS,'
            'THIS IS THE  PRICE NEW PRICE IN CANADIAN DOLLARS,'
            'USD,'
            'CAD,'
            'USD,'
            'US COMMENTS,'
            'CAD'
        )

        payload = {
            "file": upload_file,
            "columns": columns
        }

        response = self.client.post('/upload', payload, format='multipart')

        self.assertEqual(response.data['file'], file_name)

        for col in response.data['summary']:
            for test_col in self.result_values:
                if col['column'] == test_col['column']:
                    self.assertEqual(col['sum'], test_col['sum'])
                    self.assertEqual(col['avg'], test_col['avg'])

                self.result_values.pop(0)
