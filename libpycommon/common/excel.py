# -*- coding: utf-8 -*-
import xlrd
import pandas as pd

'''
def get_sheet_dict_xlrd(excel_name, sheet_names, head_lines_num, col_indexes:[int], d_colindex_2_conv_dict:dict[int, dict]):
    data = xlrd.open_workbook(excel_name)
    sheets = data.sheet_names()
    print(str(sheets))
    cols_conv = d_colindex_2_conv_dict.keys()

    ret:{str:[[]]} = {}
    for sheet_name in sheets:
        if sheet_name not in sheet_names:
            continue
        sheet = data.sheet_by_name(sheet_name)
        sheet_value:[[]] = [len(sheet.nrows) - head_lines_num]
        row_index = 0
        for rowNum in range(sheet.nrows):
            if rowNum < head_lines_num:
                continue
            rowVale = sheet.row_values(rowNum)
            row_value:[] = [len(col_indexes)]
            col_index = 0
            for colNum in range(sheet.ncols):
                if colNum not in col_indexes:
                    continue
                value = rowVale[colNum]
                if colNum in cols_conv:
                    d_conv = d_colindex_2_conv_dict[colNum]
                    value = d_conv[value]
                row_value[col_index] = value
                col_index += 1
            sheet_value[row_index] = row_value
            row_index += 1
        ret[sheet_name] = sheet_value

    return ret
'''

def get_sheet_dict_pd(excel_name, sheet_names, head_lines_num=1, usecols=None):
    if head_lines_num > 1:
        return pd.read_excel(excel_name, sheet_name=sheet_names, header=list(range(0, head_lines_num - 1)), usecols=usecols)
    else:
       return pd.read_excel(excel_name, sheet_name=sheet_names, usecols=usecols)

def write_sheet_dict_pd(excel_name, d_sheetname_df):
    # 打开excel
    writer = pd.ExcelWriter(excel_name)
    #sheets是要写入的excel工作簿名称列表
    for (sheet, output) in d_sheetname_df.items():
        output.to_excel(writer, sheet_name=sheet, index=False)
    # 保存writer中的数据至excel
    # 如果省略该语句，则数据不会写入到上边创建的excel文件中
    writer.save()
