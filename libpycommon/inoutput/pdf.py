from sqlalchemy.engine import create_engine

import pandas as pd
import time

from libpycommon.inoutput import common

def _get_engine(jdbc_alchemy, d_db):
    url = common.get_url(jdbc_alchemy, d_db)
    return create_engine(
        url,
    )

def get_by_sql(jdbc_alchemy, d_db, sql):
    engine = _get_engine(jdbc_alchemy, d_db)
    print(time.time())
    df = pd.read_sql(sql, engine)
    print(time.time())
    return df

def get_by_table_cols(jdbc_alchemy, d_db, table, cols):
    engine = _get_engine(jdbc_alchemy, d_db)
    sql = 'SELECT {} FROM {}'.format(cols, table)
    print(time.time())
    df = pd.read_sql(sql, engine)
    print(time.time())
    return df
