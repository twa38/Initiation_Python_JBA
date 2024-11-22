# coding: UTF-8
"""
Script: Initiation_Python_JBA/exo5
Création: jbaeza, le 22/11/2024
"""

# Imports

# Fonctions

# Programme principal
def main():
    # Initialiser la température extérieure
    temperature = 15


    soleil = 0


    if temperature < 5 or temperature > 25:
        print("volets fermes")
    elif temperature < 15 and soleil == 0:
        print("volets fermes")
    elif soleil == 1 and temperature > 20:
        print("volets demi fermes")
    else:
        print("volets ouverts")

if __name__ == '__main__':
    main()
# Fin
