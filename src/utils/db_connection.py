import psycopg2
from psycopg2 import pool

from .global_config import DATABASE

min_connections = 1
max_connections = 10

pool = psycopg2.pool.SimpleConnectionPool(min_connections,max_connections,**DATABASE)

def connect(query,*parameters):
    try:
        print(parameters)
        connection = pool.getconn()
        cursor = connection.cursor()
        if(parameters):
            cursor.execute(query,parameters)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        pool.putconn(connection)
        return rows

    except (Exception, psycopg2.Error) as error :
        if(connection):
            cursor.close()
            connection.close()
        return error
        