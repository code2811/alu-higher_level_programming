#!/usr/bin/python3
"""
Script to list states starting with N from a MySQL database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute query to select states starting with N, sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print results
    results = cursor.fetchall()
    for state in results:
        print(state)

    # Close database connections
    cursor.close()
    db.close()
