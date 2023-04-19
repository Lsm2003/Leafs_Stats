from sql_connection import *

def addplayer(fname, lname, position, number, country):
    sql_query = f"INSERT INTO leafs.players (first_name, last_name, position, number, country) VALUES('{fname}', '{lname}', '{position}', {number}, '{country}');"
    ExecuteAndCommit(sql_query)

def getplayers():
    sql = f"SELECT player_id, first_name, last_name, position, number, country FROM players"
    rows = ExecuteAndReturn(sql)[1]
    return rows