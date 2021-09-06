def dict_getter(keys, dict):
    from operator import itemgetter
    out = list(itemgetter(*keys)(dict))
    out = lists_concatenator(out)
    return out


def lists_concatenator(lists):
    out = []
    for list in lists:
        out += list
    return out


def read_config(file_path, line_num):
    import re
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return [re.sub(r'\s', '', i) for i in lines[line_num - 1].split(';')]


if __name__ == "__main__":
    print(lists_concatenator([["1","2"],["3","4"]]))
    print(dict_getter([1,2],{1:["1","2"],2:["3","4"]}))
