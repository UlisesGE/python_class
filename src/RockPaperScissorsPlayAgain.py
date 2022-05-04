'''
NAME
	RockPaperScissors.py
    
VERSION
    1.0
    
AUTHOR
    Hector Ulises Gaspar	
    
DESCRIPTION
	Simulación de el juego piedra papel o tijeras
    
CATEGORY
    Recreación
    
USAGE
    py src/rockpaperscissors.py
    
ARGUMENTS
    none
    
SEE ALSO
        
''' 
import random

# Pedir el nombre del usuario
print("¡El ganador es el primero en juntar 2 puntos!")
name = input("Dime tu nombre:")

# Inicializar listas y variables a ocupar
choices = ("piedra", "papel", "tijeras")
computer_score = 0
user_score = 0

while computer_score < 2 and user_score < 2:
    # Obtener elección del usuario y de la computadora
    user_choice = input(f"Ingresa una opcion, {name}: piedra, papel o tijeras \n").lower()
    computer_choice = random.choice(choices)

    # Si la opción no es valida, avisar y cerrar el programa
    if user_choice not in choices:
        print("Error, opción no válida vuelve a intentarlo")
        exit()

    # Si las opciones son iguales, sera empate
    if computer_choice == user_choice:
        print(f"El oponente eligió {computer_choice}. Empate, chanclas")

    # Primer caso elección piedra
    elif user_choice == "piedra":
        if computer_choice == "papel":
            print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
            computer_choice += 1
        if computer_choice == "tijeras":
            print(f"El oponente eligió {computer_choice}. ¡Ganaste!")
            user_score += 1

    # Segundo caso elección tijeras
    elif user_choice == "tijeras":
        if computer_choice == "piedra":
            print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
            computer_score += 1
        if computer_choice == "papel":
            print(f"El oponente eligió {computer_choice}. ¡Ganaste!")
            user_score += 1
        
    # Tercer caso elección papel
    elif user_choice == "papel":
        if computer_choice == "tijeras":
            print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
            computer_score += 1
        if computer_choice == "piedra":
            print(f"El oponente eligió {computer_choice}. ¡Ganaste!")
            user_score += 1

if user_score > computer_score:
    print(f"{name}, ganaste. Puntuacion: {user_score} a {computer_score}")

else:
    print(f"{name}, perdiste. puntuacion: {user_score} a {computer_score}")