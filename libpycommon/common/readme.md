# common

## cmd.py

### execute

```
:param cmd: 命令行内容
:param err_prompt: 错误提示
:return: 
```

## collection.py

### list_lowercased

```
每个对象lower并返回
:param mylist:可迭代对象
:return: list
```

### list_intersect

```
交集
:param a: 可迭代对象
:param b: 可迭代对象
:param lower_or_not: 是否小写
:return: list
```

### list_union

```
并集
:param a: 可迭代对象
:param b: 可迭代对象
:param lower_or_not: 是否小写
:return: list
```

### list_only_in_first

```
差集（a为基）
:param a: 可迭代对象
:param b: 可迭代对象
:param lower_or_not: 是否小写
:return: list
```

### dict_get_tuple_key_split

```
{(a,b):obj}->{a:{b:obj}}
:param d_input: 形如{(a,b):obj}字典
:return: list
```

### dict_get

```
获取字典值默认None
:param d: 字典
:param key: 键
:return: 值
```

### dict_chunk_by_size

```
把字典根据size（每个对象的大小）进行性切分，余数进入列表最后一个对象
:param dicts: 待切分字典
:param size: 切分基数
:return: list
```

### dict_chunk_by_split

```
把字典根据split（切出多少对象）进行性切分，余数进入列表最后一个对象
:param dicts: 待切分字典
:param split: 切分基数
:return: list
```



## excel.py

### get_sheet_dict_pd

```
读取excel返回DataFrame
:param excel_name: 文件名
:param sheet_names: 表单名
:param head_lines_num: 有几行表头
:param usecols: 使用列
:return: DataFrame
```

### write_sheet_dict_pd

```
写入excel
:param excel_name: 到处文件名
:param d_sheetname_df: 形如{sheetname:df}字典
:return: 
```



## excpt.py

### wait_2_exec_times

```
用于try函数运行
:param times:尝试次数 
:param secs_2sleep:失败延时时长
:param func_2wait: 函数
:param *params: 函数参数
:return: 函数运行结果
```

## misc.py

### get_env

```
获取环境变量
:param var: 环境变量
:param value_default: 默认值
:return: 环境变量值
```

### get_emptystr_if_none

```
获取对象，如果空则返回None
:param obj: 对象
:return: 对象或者None
```

### md_to_rst

```
通过rest接口转换md文件到rst
:param from_file: md文件
:param to_file: rst文件
:return: 
```

### 

## mycrypto

### create_key_pair

```
生成公私钥对
:param package_abs_path: 密钥地址
:return: 
```

### encrypt

```
加密文本
:param text: 文本
:param package_res_path: 密钥地址
:return: 加密后文本
```

### decrypt

```
解密文本
:param cipher_text: 加密后文本
:param package_res_path: 密钥地址
:return: 解密后文本
```

### sign

```
签名
:param text: 文本
:param package_res_path: 密钥地址
:return: 签名文本
```

### verify

```
签名验证
:param text: 文本
:param signature: 签名文本
:param package_res_path: 密钥地址
:return: 是否通过
```

## myhttp.py

### get_url

```
拿到网址文本
:param url_prefix: 前缀，通常是协议
:param path: 路径
:return: 网址文本
```

### get_header

```
获取表头字典
:return: {'Content-type': 'application/json'}
```

### get_text

```
拿到res对象中的文本（JSON）
:param resp: resp对象
:return: 相应文本
```

### get

```
get
:param url_prefix: 获取信息
:param auth: 认证信息
:return: res返回
```

### post

```
get
:param url_prefix: 获取信息
:param auth: 认证信息
:param req: requestdata
:return: res返回
```

### put

```
put
:param url_prefix: 获取信息
:param auth: 认证信息
:param req: requestdata
:return: res返回
```

### delete

```
delete
:param url_prefix: 获取信息
:param auth: 认证信息
:param req: requestdata
:return: res返回
```

## mylog.py

### get_logger

```
获取一个logger
:param level: 获取信息
:return: logger
```

### get_level_from_name

```
获取一个logger
:param level_name: 获取level
:return: <Logger mylog (XXX)>
```

### get_topmodname

```
获取当前模块名
:return: 根据路径体现模块
```

## mypd.py

### get_dict_2_list

```
根据a列生成b列类似reducemap的列表,
:param df: 目标df
:param tok_col: 主键列
:param tovl_col: 进入列表列
:return: dict
```

### get_dict

```
根据a列，b列生成字典，重复项只保留第一项(tok_col为基准)
:param df: 目标df
:param tok_col: 主键列
:param tovl_col: 进入列表列
:return: dict
```

### get_dict_grped_df

```
生成形如 {name1:group1}这样的字典
:param df: 目标df
:param k_col:groupby的对象
:return: dict
```

### get_tuple

```
把一条row中对应k_cols字段取出并拼成元组
:param row: 一条df记录
:param k_cols:需要的字段
:return: tuple
```

### get_tuple_key_grped_df

```
生成形如 {(c1,c2,c3):group1}这样的字典
:param df: 目标df
:param k_cols:需要当作key的字段
:return: dict
```

### get_df_append_col_by_dict

```
追加列使用字典d中的VALUE，KEY采用DF中特定列col_key，给与新列名col_new于索引号pos
:param df: 目标DF
:param col_key: 用作于KEY的列名
:param col_new: 追加列名
:param d: 映射字典
:param pos: 列的索引号
:return: df
```

### get_df_trimmed

```
把str类型做strip
:param df: 目标df
:return: dict
```

### get_df_merged

```
纵向合并多个DF
:param l_df：由DF组成的列表
:return: df
```



## mystring.py

### is_chinese

```
检查整个字符串是否包含中文
:param string: 需要检查的字符串
:return: bool
```

### is_empty

```
是否为空字符串，纯空格视为空
:param str: 需要检查的字符串
:return: bool
```

### is_valid_chinese

```
检查整个字符串是否包含中文，多了strip
:param string: 需要检查的字符串
:return: bool
```

### unicode_conv

```
解码byte类型
:param bytes_input: 需要检查bytes
:return: str
```

### is_chinese

```
检查整个字符串是否包含中文
:param string: 需要检查的字符串
:return: bool
```

### is_weird_ascii_4_tablecols

```
正则匹配文本不存在[0-9a-zA-Z_]
:param string: 需要检查的字符串
:return: bool
```



## myut.py

### all_case

```
获取测试用例
:param path: 用例相对路径
:return: 测试套件对象
```

### entry

```
获取测试用例
:param path: 用例相对路径
:return: 测试套件对象
```



# utils

## common_utils.py

### dict_getter

```
获取多个key的值，列表返回
:param keys: 需要获取的键
:param dict: 目标字典
:return: list
```

### lists_concatenator

```
链接多个可迭代对象，
:param lists: 需要链接的多个可迭代对象列表
:return: list
```

### read_config

```
读取配置文件，分号分隔，会完全读取
:param file_path: 配置文件，utf8
:param line_num: 读第几行的内容
:return: list
```

## wx_decrypt_utils.py

```待完善```

## wx_login_utils.py

```待完善```

## wx_QRcode_utils.py

```待完善```

