from sql_connection import *

def addplayer(fname, lname, position, number, country):
    sql_query = f"INSERT INTO leafs.players (first_name, last_name, position, number, country) VALUES('{fname}', '{lname}', '{position}', {number}, '{country}');"
    ExecuteAndCommit(sql_query)

def getplayers():
    sql = f"SELECT players.player_id, players.first_name, players.last_name, players.position, players.number, country FROM leafs.players"
    rows = ExecuteAndReturn(sql)[1]
    return rows

def updateplayer(id, fname, lname, position, number, country):
    sql_query = f"UPDATE leafs.players SET first_name = '{fname}', last_name = '{lname}', position = '{position}', number = {number}, country = '{country}' WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)
