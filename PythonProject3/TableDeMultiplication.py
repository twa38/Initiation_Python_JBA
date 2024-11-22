# coding: UTF-8
"""
Script: Initiation_Python_JBA/multiplication
Création: jbaeza, le 22/11/2024
"""

# Fonctions
def table():

    for i in range(1, 11):

        for j in range(1, 11):

            print(i * j, end='\t')

        print()

# Programme principal
def main():
    # Appeler la fonction table pour afficher la table de multiplication
    table()

if __name__ == '__main__':
    main()
# Fin
