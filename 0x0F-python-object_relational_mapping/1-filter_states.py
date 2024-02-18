#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db_connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    for row in db_cursor:
        print(row)

    db_cursor.close
    db_connect.close
