# -*- coding: utf-8 -*-
import redis
import os
from libpycommon.common import misc
from libpycommon.libpycommonkey.me import *

class Redis_conn():
    def __init__(self,package_key_res_path):
        self.package_key_res_path=package_key_res_path
        self.REDIS_HOST=misc.get_env('REDIS_HOST') or None
        self.REDIS_PORT=misc.get_env('REDIS_PORT') or None
        self.REDIS_MAX_CONN=misc.get_env('REDIS_MAX_CONN') or None
        try:
            self.REDIS_PASSWD=misc.get_env_encrypted('REDIS_PASSWD', self.package_key_res_path)
        except:
            self.REDIS_PASSWD=None
    def getR(self):
        pool = redis.ConnectionPool(host=self.REDIS_HOST, port=int(self.REDIS_PORT),
                                    max_connections=int(self.REDIS_MAX_CONN),
                                    password=self.REDIS_PASSWD)
        return redis.StrictRedis(connection_pool=pool, decode_responses=True)

    def getR_by_d_db(self,d_db):
        pool = redis.ConnectionPool(host=d_db['REDIS_HOST'], port=int(d_db['REDIS_PORT']),
                                    max_connections=int(d_db['REDIS_MAX_CONN']),
                                    password=misc.decrypt(d_db['REDIS_PASSWD'],self.package_key_res_path))
        return redis.StrictRedis(connection_pool=pool, decode_responses=True)







if __name__ == '__main__':#ex
    rcnn=Redis_conn(package_key_res_path)