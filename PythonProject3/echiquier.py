# coding: UTF-8
"""
Script: Initiation_Python_JBA/echiquier
Création: jbaeza, le 22/11/2024
"""

# Imports

# Fonctions
def echiquier1():

    colonnes = 'abcdefgh'

    for ligne in range(8, 0, -1):

        for colonne in colonnes:   # Boucle pour les colonnes de a à h

            print(f"{colonne}{ligne}", end=' ') # Afficher la coordonnée de la case

        print()   # Passer à la ligne suivante 

# Programme principal
def main():
    echiquier1()

if __name__ == '__main__':
    main()
# Fin
