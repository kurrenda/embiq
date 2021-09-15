from openpyxl.cell import cell as openpyxl_cell


def get_cell_merge_width_data(sheet, cell):
    for merged_cell in sheet.merged_cells.ranges:
        if (cell.coordinate in merged_cell):
            merge_width = {
                "col_min_width": merged_cell.min_col,
                "col_max_width": merged_cell.max_col
            }
            return merge_width
    return False


def get_stats(worksheet, input_columns_data):
    for col_name, col_info in input_columns_data.items():
        if col_info:
            col_start_range, col_end_range = get_columns_check_range(col_info)
            col_iterator = worksheet.iter_cols(
                min_col=col_start_range,
                max_col=col_end_range,
                min_row=col_info['row_coordinate'])
            for col in col_iterator:
                cell_sum = 0
                for cell in col:
                    if cell.data_type == openpyxl_cell.TYPE_NUMERIC:
                        if cell.value:
                            cell_sum += cell.value
                print(cell, cell_sum)


def get_columns_check_range(column_info):
    columns_to_check = []
    if 'merge_width' in column_info:
        width = column_info['merge_width']
        if {'col_min_width', 'col_max_width'} <= set(width):
            for col in range(width['col_min_width'], width['col_max_width']):
                columns_to_check.append(col)
    else:
        if 'col_coordinate' in column_info:
            columns_to_check.append(column_info['col_coordinate'])

    start_column = min(columns_to_check)
    end_column = max(columns_to_check)

    return start_column, end_column
