# coding: UTF-8
"""
Script: Initiation_Python_JBA/echiquier
Création: jbaeza, le 22/11/2024
"""

# Fonctions
def echiquier2(colonne, ligne):


    for l in '87654321':

        for c in 'abcdefgh':

            if c == colonne and l == ligne:
                print('*', end=' ')
            else:
                print('-', end=' ')

        print()

# Programme principal


if __name__ == '__main__':
    print("nique zebis :")
    echiquier2('h', '1')
# Fin
