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

print("¡El ganador es el primero en juntar 2 puntos!")
name = input("Dime tu nombre:")

choices = ("piedra", "papel", "tijeras")
computer_score = 0
user_score = 0

user_choice = input(f"Ingresa una opcion, {name}: piedra, papel o tijeras \n").lower()
computer_choice = random.choice(choices)

if computer_choice == user_choice:
    print(f"El oponente eligió {computer_choice}. Empate, chanclas")
          
elif user_choice == "piedra":
    if computer_choice == "papel":
        print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
    if computer_choice == "tijeras":
        print(f"El oponente eligió {computer_choice}. ¡Ganaste!")

elif user_choice == "tijeras":
    if computer_choice == "piedra":
        print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
    if computer_choice == "papel":
        print(f"El oponente eligió {computer_choice}. ¡Ganaste!")

elif user_choice == "papel":
    if computer_choice == "tijeras":
        print(f"El oponente eligió {computer_choice}. Perdiste banda :(")
    if computer_choice == "piedra":
        print(f"El oponente eligió {computer_choice}. ¡Ganaste!")

