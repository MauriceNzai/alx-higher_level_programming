#!/usr/bin/python3
# gets all cities


def main(args):
    """
    Gets all cities
    """
    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(host = "localhost", user = args[1],
                        passwd = args[2], db = args[3])
    cur = db.cursor()
    cur.execute(
            "SELECT c.id, c.name, s.name FROM cities c JOIN states s\
                    ON s.id = c.state_id ORDER BY c.id",
            .format(args[4]))
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
