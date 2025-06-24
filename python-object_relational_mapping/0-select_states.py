#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def main():
    """Connects to the database and prints all states ordered by id."""
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur et exécution de la requête
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    # Affichage des résultats
    for row in rows:
        print(row)

    # Fermeture propre
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
