#!/usr/bin/python3
"""
contains a function main() that gets all states that  rgument passse by user
"""


def main(args):
    """
    Gets all states that match user's argument
    """
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(
            host="localhost", user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name like '{}' ORDER BY id ASC",
            .format(args[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == state[4]:
            print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
