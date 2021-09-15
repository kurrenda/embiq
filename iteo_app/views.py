from io import BytesIO
import openpyxl

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from iteo_app import serializers, excel_finder


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = serializers.FileSerializer(data=request.data)
        if serializer.is_valid():
            file_obj = request.data['file']

            workbook = openpyxl.load_workbook(BytesIO(file_obj.read()))
            sheets = workbook.sheetnames
            worksheet = workbook[sheets[0]]

            input_columns = [x.strip() for x in request.data['columns'].split(',')]
            input_columns_data = dict.fromkeys(input_columns, None)
            
            row_count = worksheet.max_row
            column_count = worksheet.max_column

            for input_col, input_col_val in input_columns_data.items():
                for worksheet_row in worksheet.iter_rows(1, row_count):
                    for worksheet_col in worksheet_row:
                        if input_col == worksheet_col.value:
                            header_column_info = {}
                            merge_width_data = excel_finder.get_cell_merge_width_data(
                                worksheet,
                                worksheet_col
                            )
                            if merge_width_data:
                                header_column_info['merge_width'] = merge_width_data

                            header_column_info['col_coordinate'] = worksheet_col.column
                            header_column_info['row_coordinate'] = worksheet_col.row
                            input_columns_data[input_col] = header_column_info
                            break
            excel_finder.get_stats(worksheet, input_columns_data)
            return Response(input_columns_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
