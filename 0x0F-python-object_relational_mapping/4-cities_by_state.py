#!/usr/bin/python3

"""
script that lists all cities from the database hbtn_0e_4_usa.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db_connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3],
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        join states ON cities.state_id=states.id
        """
        )

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db_connect.close()
