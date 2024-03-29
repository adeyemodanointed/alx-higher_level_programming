#!/usr/bin/python3
"""
Script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
Use the module MySQLdb (import MySQLdb)
Script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print("MySQL Error: %s" % str(e))

    for row in rows:
        print(row)

    cur.close()
    db.close()
