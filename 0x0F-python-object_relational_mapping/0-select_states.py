#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
the script takes 3 arguments
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host = 'localhost', port = 3306, user = username, passwd = password, db = db_name)
    cursor = db.cursor() #CREATE A cursor object
    cursor.execute("SELECT * FROM STATES ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

