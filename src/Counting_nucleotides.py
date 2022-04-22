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
         python Counting_nucleotides.py


ARGUMENTS
       Ninguno

    
SEE ALSO
        Ninguno

'''
#Se lee una secuencia del usuario del teclad+o
secuencia = input('Introduce una secuencia:\n')

# Realizar conteo de cada base
freq_A = secuencia.count('A')
freq_C = secuencia.count('C')
freq_G = secuencia.count('G')
freq_T = secuencia.count('T')

# Imprimir el resultado
print(f"""El numero de A es: {freq_A}
El numero de C es: {freq_C}  
El numero de G es: {freq_G}  
El numero de T es: {freq_T}""")
