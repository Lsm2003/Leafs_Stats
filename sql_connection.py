import mysql.connector
import sql_login


def ExecuteAndCommit(query):
    with mysql.connector.connect(host='localhost', user=sql_login.user, password=sql_login.password, database='leafs') as mysql_connection:
        with mysql_connection.cursor() as mysql_cursor:
            mysql_cursor.execute(query)
            mysql_connection.commit()
            return mysql_cursor.rowcount


def ExecuteAndReturn(query):
    with mysql.connector.connect(host='localhost', user=sql_login.user, password=sql_login.password, database='leafs') as mysql_connection:
        with mysql_connection.cursor() as mysql_cursor:
            mysql_cursor.execute(query)
            return mysql_cursor.column_names, mysql_cursor.fetchall()