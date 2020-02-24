from .global_config import DATABASE
import psycopg2

def connect(query):
    try:
        connection = psycopg2.connect(user = DATABASE['user'],
                                    password = DATABASE['password'],
                                    host = DATABASE['host'],
                                    port = DATABASE['port'],
                                    database = DATABASE['database'])

        cursor = connection.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        cursor.close()
        connection.close()
        return record

    except (Exception, psycopg2.Error) as error :
        if(connection):
            cursor.close()
            connection.close()
        return error
        