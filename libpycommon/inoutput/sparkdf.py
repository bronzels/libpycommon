from libpycommon.inoutput import constant
from libpycommon.inoutput import common


def get_properties(jdbc_driver, d_db):
    properties = {}
    properties[constant.jdbc_connection_keyname_driver] = jdbc_driver
    properties[constant.jdbc_connection_keyname_user] = d_db[constant.jdbc_connection_keyname_user]
    properties[constant.jdbc_connection_keyname_password] = d_db[constant.jdbc_connection_keyname_password]
    return properties


def get_by_sql(spark_session, jdbc_alchemy, jdbc_driver, d_db, sql):
    wrapped_sql = '({}) AS temp_sql'.format(sql)
    url = common.get_jdbc(jdbc_alchemy, d_db)
    properties = get_properties(jdbc_driver, d_db)
    jdbc_df = spark_session \
        .read \
        .jdbc(
        url,
        wrapped_sql,
        # 'social.blog',
        properties=properties
    )
    return jdbc_df


def get_by_sql_wt_pt(spark_session, jdbc_alchemy, jdbc_driver, d_db, sql, partition_col, partitions, lower_bound, upper_bound):
    wrapped_sql = '({}) AS temp_sql'.format(sql)
    url = common.get_jdbc(jdbc_alchemy, d_db)
    properties = get_properties(jdbc_driver, d_db)
    jdbc_df = spark_session \
        .read \
        .jdbc(
        url,
        wrapped_sql,
        column=partition_col,
        lowerBound=lower_bound,
        upperBound=upper_bound,
        numPartitions=partitions,
        properties=properties
    )
    return jdbc_df


def get_by_table_cols(spark_session, jdbc_alchemy, jdbc_driver, d_db, table, cols, partition_col, sql_limit, partitions):
    cols.append(partition_col)
    if sql_limit == -1:
        partition_sql = 'SELECT MIN({1}) AS minpt, MAX({1}) AS maxpt FROM {0}'.format(table, partition_col)
    else:
        partition_sql = 'SELECT MIN({1}) AS minpt, MAX({1}) AS maxpt FROM (SELECT {1} FROM {0} ORDER BY {1} LIMIT {2}) temp_limited'.format(table, partition_col, sql_limit)
    bound_row_df = get_by_sql(spark_session, jdbc_alchemy, jdbc_driver, d_db, partition_sql)
    bound_row = bound_row_df.first()
    lower_bound = bound_row['minpt']
    if lower_bound is None:
        lower_bound = 0
    upper_bound = bound_row['maxpt']
    if upper_bound is None:
        upper_bound = 0
    if sql_limit == -1:
        sql = 'SELECT {0} FROM {1}'.format(', '.join(cols), table)
    else:
        sql = 'SELECT {0} FROM {1} ORDER BY {2} LIMIT {3}'.format(', '.join(cols), table, partition_col, sql_limit)
    partition_df = get_by_sql_wt_pt(spark_session, jdbc_alchemy, jdbc_driver, d_db, sql, partition_col, partitions, lower_bound,
                            upper_bound)
    return partition_df.drop(partition_col)


def get_by_sql_cols(spark_session, jdbc_alchemy, jdbc_driver, d_db, sql, partition_col, partitions):
    partition_sql = 'SELECT MIN({1}) AS minpt, MAX({1}) AS maxpt FROM ({0}) temp'.format(sql, partition_col)
    bound_row_df = get_by_sql(spark_session, jdbc_alchemy, jdbc_driver, d_db, partition_sql)
    bound_row = bound_row_df.first()
    lower_bound = bound_row['minpt']
    if lower_bound is None:
        lower_bound = 0
    upper_bound = bound_row['maxpt']
    if upper_bound is None:
        upper_bound = 0
    partition_df = get_by_sql_wt_pt(spark_session, jdbc_alchemy, jdbc_driver, d_db, sql, partition_col, partitions, lower_bound,
                            upper_bound)
    return partition_df.drop(partition_col)

def set_df_overwrite(jdbc_alchemy, jdbc_driver, d_db, df, table_name):
    url = common.get_jdbc(jdbc_alchemy, d_db)
    properties = get_properties(jdbc_driver, d_db)
    df.write.jdbc(url=url, table=table_name, mode='overwrite', properties=properties)

def set_df_truncate(jdbc_alchemy, jdbc_driver, d_db, df, table_name):
    url = common.get_jdbc(jdbc_alchemy, d_db)
    properties = get_properties(jdbc_driver, d_db)
    df.write.option("truncate", "true").jdbc(url=url, table=table_name, mode='overwrite', properties=properties)

def set_df_append(jdbc_alchemy, jdbc_driver, d_db, df, table_name):
    url = common.get_jdbc(jdbc_alchemy, d_db)
    properties = get_properties(jdbc_driver, d_db)
    df.write.jdbc(url=url, table=table_name, mode='append', properties=properties)
