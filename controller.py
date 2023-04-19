from sql_connection import *

def addToPlayer(fname, lname, position, number, country):
    sql_query = f"INSERT INTO leafs.players (first_name, last_name, position, number, country) VALUES('{fname}', '{lname}', '{position}', {number}, '{country}');"
    ExecuteAndCommit(sql_query)

def getplayers():
    sql = f"SELECT players.player_id, players.first_name, players.last_name, players.position, players.number, country FROM leafs.players"
    rows = ExecuteAndReturn(sql)[1]
    return rows

def updateplayer(id, fname, lname, position, number, country):
    sql_query = f"UPDATE leafs.players SET first_name = '{fname}', last_name = '{lname}', position = '{position}', number = {number}, country = '{country}' WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)

def addToStats(lname):
    sql_query = f"INSERT INTO leafs.stats (player_name, goals, assists, points) VALUES('{lname}', 0, 0, 0);"
    ExecuteAndCommit(sql_query)


def deleteFromPlayer(id):
    sql_query = f"DELETE FROM leafs.players WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)


def deleteFromStats(id):
    sql_query = f"DELETE FROM leafs.stats WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)