from sql_connection import *

def addToPlayer(fname, lname, position, number, country):
    sql_query = f"INSERT INTO leafs.players (first_name, last_name, position, number, country) VALUES('{fname}', '{lname}', '{position}', {number}, '{country}');"
    ExecuteAndCommit(sql_query)

def getplayers():
    sql_query = f"SELECT players.player_id, players.first_name, players.last_name, players.position, players.number, country FROM leafs.players"
    rows = ExecuteAndReturn(sql_query)[1]
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

def getStats():
    sql_query = f"SELECT stats.player_id, stats.player_name, stats.goals, stats.assists, stats.points FROM leafs.stats"
    rows = ExecuteAndReturn(sql_query)[1]
    return rows

def updateStats(id, goals, assists, points):
    sql_query = f"UPDATE leafs.stats SET goals = {goals}, assists = {assists}, points = {points} WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)

def getAllStats():
    sql_query = f"SELECT stats.player_id, stats.player_name, stats.goals, stats.assists, stats.points FROM leafs.stats"
    return ExecuteAndReturn(sql_query)

def getAllPlayers():
    sql_query = f"SELECT players.player_id AS 'ID', players.first_name AS 'First Name', players.last_name AS 'Last Name', players.position AS 'Position', players.number AS 'Number', players.country AS 'country' FROM leafs.players;"
    return ExecuteAndReturn(sql_query)

def updatePlayerInStats(id, name):
    sql_query = f"UPDATE leafs.stats SET player_name = '{name}' WHERE player_id = {id}"
    ExecuteAndCommit(sql_query)

