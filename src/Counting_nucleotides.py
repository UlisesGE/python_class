'''NAME
       counting_nucleotides

VERSION
        1.2

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Cuenta la cantidad de A, T G y C de una secuencia dada de DNA.

CATEGORY
        Script

USAGE
         py src/Counting_nucleotides.py


ARGUMENTS
    Ninguno

    
SEE ALSO
        Ninguno


'''
#Se lee una secuencia del usuario del teclad+o
secuencia = input('Introduce una secuencia:\n')

#Se cuenta y se imprime la cantidad de cada letra de la secuencia
print("Numero de G:", secuencia.count("G"))
print("Numero de A:", secuencia.count("A"))
print("Numero de T:", secuencia.count("T"))
print("Numero de C:", secuencia.count("C"))