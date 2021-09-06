# -*- coding: utf-8 -*-

def list_lowercased(mylist):
    return list(map(lambda x: x.lower(), mylist))

def list_intersect(a, b, lower_or_not:bool=False):
    if lower_or_not:
        a = list_lowercased(a)
        b = list_lowercased(b)
    return list(set(a) & set(b))

def list_union(a, b, lower_or_not:bool=False):
    if lower_or_not:
        a = list_lowercased(a)
        b = list_lowercased(b)
    return list(set(a).union(set(b)))

def list_only_in_first(a, b, lower_or_not:bool=False):
    if lower_or_not:
        a = list_lowercased(a)
        b = list_lowercased(b)
    return list(set(a).difference(set(b)))

def list_if_first_all_in_second(a, b):
    return len(set(a) - set(b)) == 0

def dict_get_tuple_key_split(d_input):
    ret = {}
    for(k, v) in d_input.items():
        if ret.get(k[0]) is None:
            ret[k[0]] = {}
        ret[k[0]][k[1]] = v
    return ret

def dict_get(d, key):
    if d is None:
        return None
    else: return d.get(key)

def dict_chunk_by_size(dicts, size):
    new_list = []
    dict_len = len(dicts)
    # 获取分组数
    while_count = dict_len // size + 1 if dict_len % size != 0 else dict_len / size
    split_start = 0
    split_end = size
    while (while_count > 0):
        #把字典的键放到列表中，然后根据偏移量拆分字典
        new_list.append({k: dicts[k] for k in list(dicts.keys())[split_start:split_end]})
        split_start += size
        split_end += size
        while_count -= 1
    return new_list

def dict_chunk_by_split(dicts, split):
    new_list = []
    dict_len = len(dicts)
    size = dict_len // split if dict_len % split == 0 else dict_len // split + 1
    # 获取分组数
    split_start = 0
    split_end = size
    while (split > 0):
        #把字典的键放到列表中，然后根据偏移量拆分字典
        new_list.append({k: dicts[k] for k in list(dicts.keys())[split_start:split_end]})
        split_start += size
        split_end += size
        split -= 1
    return new_list
