# Mis notas de la materia de Python I

__Nombre:__ Ulises Gaspar Gen.19

*Fecha: 03/03/2022*

[LCG](https://www.lcg.unam.mx/

Institución:  <img title="" src="file:///D:/Downloads/lcg.png" alt="" width="120" height="50">

## Tema: Markdown

### ¿Qué es Markdown?

- Lenguaje de marcado

- Basado en texto plano

- Fácil de exportar a otros formatos

Ejemplo de marcado de código:

`int nombre();`

```
///esto es un bloque de código
var x=l;
```

| Formato   | Etiqueta |
| --------- | -------- |
| Título    | `#`      |
| Subtítulo | `##`     |

## Github

alquicir@ccg.unam.mx - Shirley

### Introducción

**Vamos a comenzar a hacer software, pero ¿qué queremos lograr con el desarollo de software?**

- Resolver algún problema

- Que nuestro código pueda ser utilizado por otras personas

- Que el software sea fácil de entender por mi y por los demás 

- Que sea fácil realizar modificaciones

- Colalborar con más gente

__Para lograrlo se necesita:__

- Utilizar estándares de codificación
  
  - PEP8 para Python
  
  - Guías de estilo de Google

- Utilizar notaciones o estándares de nombrado
  
  - Camel case
  
  - Upper case

- Buenas prácticas
  
  - Encabezado de programas
  
  - Documentación interna
  
  - Nombrado adecuado de variables y métodos/funciones
  
  - Nombrado adecuado de los programas
  
  - Organización adecuada del código (carpetas y archivos)
  
  - Compartir el código con mis compañeros para obtener retroalimentación

- Control de versiones de código
  
  - Forma manual: El versionamiento está constituido por dos dígitos, versiones primarias y secundaias (X.Y), 
    
    v 1.8
    
        X (major): Cuando el programa se considere liberado estable. La versión principal cambiará y la varsión secundaria quedará en cero.
    
        Y (minor): la versión se
  
  - Forma automática: por medio de un sistema de control de versiones. Esto es una herramienta que se encarga por nosotros de controlar todos los cambios que realicemos en nuestros programas, creando diferentes versiones de nuestros archivos. 
  
  - 

### Git

**Git de manera local:**

- Solo yo puedo tener acceso al código

- Puedo controlar en mi computadora los cambios que haga el código

- Mi software se vuelve de uso personal

**Git + GitHub:**

- Permitiendo trabajar conjuntamente en una idea

- Formar una comunidad de varias personas trabajando en un fin común

- Contribuir a mejorar un código

- Acceso al código, leerlo, estudiarlo y aprender de él, e incluso hacer cambios y experimentar sin afectar el código original. 

17/02/2022

`git diff`

Una modificación contra la versión previa de los commits. 

`git diff --staged`

Compara con el último **commit add**, no cualquier modificación. 

`git log` lista todos los commits realizados en el repositorio en orden cronológico inverso.

`git log -N` donde `N` indica el número de commits que queremos obtener.

`git status` nos dice si hace falta hacer un commit

`git log --oneline` solo da el identificador en su forma corta, y el mensaje que se asoció al commit

**Ramas de git:** 

Una rama de Git es un apuntador que nos permitirá hacer referencia a cada una de las confirmaciones (commits). La rama por defecto de Gir es la rama master. 

##Git y GitHub
