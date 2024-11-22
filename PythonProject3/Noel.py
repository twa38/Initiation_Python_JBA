# coding: UTF-8
"""
Script: Initiation_Python_JBA/noel
Création: jbaeza, le 22/11/2024
"""

# Fonctions
def sapin(hauteur):


    for i in range(1, hauteur + 1):

        print((hauteur-i) * ' ', '* ' * i)


    for j in range(hauteur // 2):
        print((hauteur-2) * ' ', '| |')


if __name__ == '__main__':
    print("Sapin :")
    sapin(9)
    print()

# Fin
