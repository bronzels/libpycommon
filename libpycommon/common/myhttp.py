# -*- coding: utf-8 -*-
import requests
import json

from libpycommon.common.mylog import *

def get_url(url_prefix, path):
    return '{}{}'.format(url_prefix, path)

def get_header():
    req_header = {}
    req_header['Content-type'] = 'application/json'
    return req_header

def get_text(resp):
    code = resp.status_code
    logger.debug(code)
    if code == 200:
        text = json.loads(resp.text)
        #logger.debug(text)
        return text
    elif code == 204:
        return resp.text
    else:
        raise Exception('wrong resp:{}'.format(resp.content.decode('UTF-8')))
        #logger.debug('Wrong HTTP resp:{}'.format(resp.content.decode('UTF-8')))
        #return None

def get(url_prefix, auth, path):
    req_url = get_url(url_prefix, path)
    req_header = get_header()
    logger.debug('path:{}'.format(path))
    resp = requests.get(req_url, auth=auth, headers=req_header)
    return get_text(resp)

def post(url_prefix, auth, path, req):
    req_url = get_url(url_prefix, path)
    req_header = get_header()
    logger.debug('path:{}, req:{}'.format(path, req))
    resp = requests.post(req_url, auth=auth, headers=req_header, data=json.dumps(req), verify=False)
    return get_text(resp)

def put(url_prefix, auth, path, req):
    req_url = get_url(url_prefix, path)
    req_header = get_header()
    logger.debug('path:{}, req:{}'.format(path, req))
    resp = requests.put(req_url, auth=auth, headers=req_header, data=json.dumps(req), verify=False)
    return get_text(resp)

def delete(url_prefix, auth, path, req):
    req_url = get_url(url_prefix, path)
    req_header = get_header()
    logger.debug('path:{}, req:{}'.format(path, req))
    resp = requests.delete(req_url, auth=auth, headers=req_header, data=json.dumps(req), verify=False)
    return get_text(resp)
