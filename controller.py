from sql_connection import *

def addplayer(fname, lname, position, number, country):
    sql_query = f'INSERT INTO leafs.players VALUES("{fname}", "{lname}", "{position}", {number}, "{country}")'
    ExecuteAndCommit(sql_query)

def getplayers():
    sql = f"SELECT player_id, last_name FROM players"
    rows = ExecuteAndReturn(sql)[1]
    return rows