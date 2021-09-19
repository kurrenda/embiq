from io import BytesIO

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from iteo_app import serializers
from iteo_app.excel import calculator, responses_schema


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description=(
            'Upload excel file with the column names '
            'to get summarized and average value for this columns'),
        operation_id='Get summarized and average values from excel file',
        manual_parameters=[
            openapi.Parameter(
                name="file",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="Excel file (allowed extensions: 'xls','xlsx')"
            ),
            openapi.Parameter(
                name="columns",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=True,
                description=(
                    "Columns whose values ​​will be counted, "
                    "separated by comma (eg. 'column1, column2')")
            )
        ],
        responses=responses_schema.response_schema_dict,
    )
    def post(self, request, format=None):
        serializer = serializers.FileSerializer(data=request.data)
        if serializer.is_valid():
            file = request.data['file']
            columns = request.data['columns']

            file_bytes = BytesIO(file.read())
            calc = calculator.ExcelCalc(file.name, file_bytes, columns)

            response = calc.compute_data()
            return Response(response)

        return Response(serializer.errors.values(),
                        status=status.HTTP_400_BAD_REQUEST)
