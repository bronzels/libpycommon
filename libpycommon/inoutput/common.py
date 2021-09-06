from libpycommon.inoutput import constant

def get_url(jdbc_alchemy, d_db):
    if jdbc_alchemy == constant.jdbc_alchemy_mssql:
        fmt = '{}://{}:{};database={}'
    else:
        fmt = '{}://{}:{}/{}'
    return fmt \
        .format(jdbc_alchemy,
                d_db[constant.jdbc_connection_keyname_host],
                int(d_db[constant.jdbc_connection_keyname_port]),
                d_db[constant.jdbc_connection_keyname_catalog])

def get_jdbc(jdbc_alchemy, d_db):
    return 'jdbc:' + get_url(jdbc_alchemy, d_db)

