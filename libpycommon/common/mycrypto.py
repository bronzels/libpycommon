# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from importlib import resources

from libpycommon.common.mylog import *

def create_key_pair(package_abs_path):
    logger.debug('1、生成 private key and pulic key')
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()
    with open(package_abs_path + 'master-private.pem', 'wb') as f:
        f.write(private_pem)
        f.close()

    public_pem = rsa.publickey().exportKey()
    with open(package_abs_path + 'master-public.pem', 'wb') as f:
        f.write(public_pem)
        f.close()

    # ghost的秘钥对的生成
    private_pem = rsa.exportKey()
    with open(package_abs_path + 'ghost-private.pem', 'wb') as f:
        f.write(private_pem)
        f.close()

    public_pem = rsa.publickey().exportKey()
    with open(package_abs_path + 'ghost-public.pem', 'wb') as f:
        f.write(public_pem)
        f.close()

def encrypt(text, package_res_path):
    f = resources.open_binary(package_res_path, 'ghost-public.pem')
    key = f.read()
    f.close()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(text.encode())).decode()
    return cipher_text

def decrypt(cipher_text, package_res_path):
    f = resources.open_binary(package_res_path, 'ghost-private.pem')
    key = f.read()
    f.close()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    random_generator = Random.new().read
    '''
    res = []
    for i in range(0, len(cipher_text), 128):
        res.append(cipher.decrypt(cipher_text[i:i + 128], 'xyz'))
    text = "".join(res)
    '''
    text = cipher.decrypt(base64.b64decode(cipher_text), random_generator).decode()
    return text

def sign(text, package_res_path):
    f = resources.open_binary(package_res_path, 'master-private.pem')
    key = f.read()
    f.close()
    rsakey = RSA.importKey(key)
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(text.encode())
    sign = signer.sign(digest)
    signature = base64.b64encode(sign).decode()
    return signature

def verify(text, signature, package_res_path):
    f = resources.open_binary(package_res_path, 'master-public.pem')
    key = f.read()
    f.close()
    rsakey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(text.encode())
    is_verify = verifier.verify(digest, base64.b64decode(signature.encode()))
    return is_verify
