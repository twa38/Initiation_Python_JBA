# coding: UTF-8
"""
Script: Initiation_Python_JBA/echiquier
Création: jbaeza, le 22/11/2024
"""

# Fonctions
def echiquier2(colonne, ligne):
    # Définir les lettres des colonnes
    colonnes = 'abcdefgh'

    # Boucle pour les lignes de 8 à 1
    for l in range(8, 0, -1):
        # Boucle pour les colonnes de a à h
        for c in colonnes:
            # Vérifier si la case correspond aux paramètres envoyés
            if c == colonne and l == ligne:
                print('*', end=' ')
            else:
                print('-', end=' ')

        print()

# Programme principal
def main():
    # Tester la fonction echiquier2 avec les valeurs colonne = 'd' et ligne = 3
    print("Affichage de l'échiquier avec une * sur la case d3 :")
    echiquier2('d', 3)

if __name__ == '__main__':
    main()
# Fin
