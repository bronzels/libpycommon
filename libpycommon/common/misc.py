import os
import requests
from libpycommon.common.mycrypto import decrypt


def get_env(var, value_default=''):
    env_dist = os.environ
    ret = env_dist.get(var, value_default)
    return ret

def get_env_encrypted(var, key_res_path, value_default=''):
    env_dist = os.environ
    ret = decrypt(env_dist.get(var, value_default), key_res_path)
    return ret

def get_emptystr_if_none(obj):
    return obj if obj is not None else ''

# 将markdown格式转换为rst格式
def md_to_rst(from_file, to_file):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to': 'rst', 'from': 'markdown'},
                      files={'input_files[]': open(from_file, 'rb')})
    if r.ok:
        with open(to_file, "wb") as f:
            f.write(r.content)
