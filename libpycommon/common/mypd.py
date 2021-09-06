# -*- coding: utf-8 -*-
import copy
from pandas.api.types import is_string_dtype

def get_dict_2_list(df, tok_col, tovl_col):
    ret = {}
    for (key, df_grped) in df.groupby(tok_col):
        ret[key] = df_grped[tovl_col].tolist()
    return ret

def get_dict(df, k_col, v_col):
    dff = df[[k_col, v_col]]  # 取出其中两列
    dff = dff.drop_duplicates(subset=[k_col], keep='first')  # 如果有重复项，需要去除，确定是保存那一列，否则会用后面的替换掉前面的
    dff.set_index(keys=k_col, inplace=True)  # 设置作为key的列为index
    dff = dff.T  # 取它的转置
    dic = dff.to_dict(orient='records')[0]  # 转化成字典，这可能会有多行，导出是一个字典类型的数组，我们取第一项就可以了
    return dic

def get_dict_grped_df(df, k_col):
    l_tuple_key_df_grped_by = df.groupby(k_col)
    d = {}
    for (value_k_col, df_grped) in l_tuple_key_df_grped_by:
        d[value_k_col] = df_grped
    return d

def get_tuple(row, k_cols):
    l = []
    for k_col in k_cols:
        l.append(row[k_col])
    return tuple(l)

def get_tuple_key_grped_df(df, *k_cols):
    tuple_df = copy.deepcopy(df)
    tuple_df.insert(loc=0, column='tuple_key_col', value=tuple_df.apply(
        lambda x: get_tuple(x, k_cols), axis='columns'))
    return get_dict_grped_df(tuple_df, 'tuple_key_col')

def get_df_append_col_by_dict(df, col_key, col_new, d, pos):
    df.insert(loc=pos, column=col_new, value=df.apply(
        lambda x: d[x[col_key]], axis='columns'))

def get_df_trimmed(df):
    def trim(input):
        if isinstance(input, str):
            return input.strip() if input is not None else None
        else: return input
    for col in [column for column in df]:
        if is_string_dtype(df[col]):
            df[col] = df.apply(lambda x: trim(x[col]), axis=1)

def get_df_merged(l_df):
    return l_df[0].append(l_df[1:len(l_df)])


