# coding: UTF-8
"""
Script: Initiation_Python_JBA/exo4
Création: jbaeza, le 22/11/2024
"""

# Imports

# Fonctions

# Programme principal
def main():
    # Demander à l'utilisateur d'entrer son âge
    age = int(input("Entrez votre âge : "))

    # Vérifier l'âge et afficher le message approprié
    if age < 16:
        print(f"Vous avez {age} ans, vous ne pouvez passer aucun permis de conduire.")
    elif 16 <= age < 18:
        print(f"Vous avez {age} ans, vous ne pouvez passer que le permis de conduire A1.")
    else:
        print("Vous êtes majeur, vous pouvez passer tous les permis de conduire.")

if __name__ == '__main__':
    main()
# Fin
