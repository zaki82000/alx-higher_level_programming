#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa"""

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
        SELECT cities.name FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
        """,
        (argv[4])
        )

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db_connect.close()
