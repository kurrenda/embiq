from io import BytesIO
import openpyxl

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from iteo_app import serializers
from iteo_app.excel import calculator


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = serializers.FileSerializer(data=request.data)
        if serializer.is_valid():
            file = request.data['file']
            columns = request.data['columns']

            file_bytes = BytesIO(file.read())
            calc = calculator.ExcelCalc(file.name, file_bytes, columns)

            response = calc.compute_data()
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)