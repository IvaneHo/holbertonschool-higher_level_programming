#!/usr/bin/python3
# Fonction pour lire un fichier texte (UTF8) et afficher le contenu dans la console

def read_file(filename=""):
    """Affiche le contenu du fichier texte donné (UTF-8) sans ajouter de saut de ligne supplémentaire."""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
