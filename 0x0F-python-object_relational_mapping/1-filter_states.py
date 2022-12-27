#!/usr/bin/python3
"""
contains a function main() that gets all states that start with N via python
"""


def main(args):
    """
    Gets all states that start by N
    """
    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(
        host="localhost", user=args[1], passwd="args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name like binary 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
