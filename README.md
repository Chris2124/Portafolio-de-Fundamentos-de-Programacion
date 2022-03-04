# ¿Qué es Python?
En términos técnicos, Python es un lenguaje de programación interpretado multiplataformas, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.
# ¿Qué es una variable?
Es un nombre que se refiere a un objeto que reside en la memoria. El objeto puede ser de alguno de los tipos vistos (número o cadena de texto), o alguno de los otros tipos existentes en Python.
Cada variable debe tener un nombre único llamado identificador. Eso es muy de ayuda pensar las variables como contenedores que contienen data el cual puede ser cambiado después a través de técnicas de programación.
## Nombrando una variable
Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o números al principio.
```phyton
#Válido 
Valor=10
Valor_1=10
Va_lor=10
VALOR=10
variable1=10
```
Los siguientes ejemplos no son correctos: 
```phyton
#No valido
2Valor=10	
Va-lor=10	
Va lor=10
Año=10
```
## Asignando valores a una variable
Al crear una variable debemos asignarle un valor para desarrollar más líneas de código en base a estas. A continuación, se creará tres variables a modo de ejemplo. Una de tipo cadenas de caracteres, otra de tipo entero y la última de tipo entero float:
```phyton
#cadenas de caracteres
c=”hola que tal”
#comprobar tipo de dato 
print(type(c))
[output] <class 'str'>
```
```phyton	
#número entero 
a=30
#comprobar tipo de dato 
print(type(a))
[output]  <class 'int'>
```
```phyton
#número decimal 
s=3.5
#comprobar tipo de dato 
print(type(s))
[output]  <class 'float'>
```
También es posible asignar múltiples valores a distintas variables en una misma línea de código, por ejemplo: 
```phyton
a, b, c = 5, 3.2, "Hola"
#impriminos la primara variable
print a
[output] 5
#impriminos la segunda variable
print b
[output] 3.2
#impriminos la tercera variable
print c
[output] Hola 
```
## Operadores básicos
Los operadores aritméticos, son los más frecuentes que nos podemos hallar, y nos permiten realizar operaciones aritméticas sencillas, como pueden ser la suma, resta, la multiplicación, etc.
### Suma
El operador “+” suma los números que se encuentran a la izquierda y derecha del operador. Se hace mención lo de números porque no tendría sentido sumar dos cadenas de texto, o dos listas, pero en Python es posible hacer este tipo de cosas.	
```phyton
#formulación de la operación 
x=4+3
#imprimimos el resultado
print(x)
[output] 7 
```
### Resta
El operador - resta los números presentes a la izquierda y derecha del operador. A diferencia el operador + en esta situación no podemos restar cadenas o listas.
```phyton
#formulación de la operación 
x=4-3
#imprimimos el resultado
print(x)
[output] 1
```
### Multiplicación
El operador * multiplica los valores de tipo de datos numéricos.
```phyton
#formulación de la operación 
x=4*3
print(x)
#imprimimos el resultado
[output] 12
```
### División
El operador / divide los números presentes a la izquierda y derecha del operador.
```phyton
#formulación de la operación 
x=4/3
print(x)
#imprimimos el resultado
[output] 1.3333333333333333
```
### Módulo
El operador % realiza la operación módulo entre los números presentes a la izquierda y la derecha. Se trata de calcular el residuo de la división entera entre ambos números.
```phyton
#formulación de la operación 
x=4%3
print(x)
#imprimimos el resultado
[output] 1
```
# Tipos de datos en Python

## Integer
Los datos integer o enteros permiten almacenar un valor numérico no decimal ya sea positivo o negativo de cualquier valor. La función type() nos restituye el tipo de la variable, y podemos distinguir como efectivamente es de la clase “int”.  
```phyton
t=13
#comprobar tipo de dato 
print(type(t))
[output] <class 'int'>
```
Es posible convertir a “int” a otro tipo. El tipo int no puedo contener decimales puesto que, si intentamos convertir un número decimal, se redondeará todo lo que tengamos a la derecha de la coma.
```phyton
#creamos una variable decimal con la función int()
b = int(1.6)
print(b) 
[output] 1
```
## Float
El tipo de dato float nos ayuda a representar un número positivo o negativo con decimales, es decir, números reales. Entonces, si declaramos una variable y le asignamos un valor decimal, por defecto la variable será de tipo float.
```phyton
f = 0.10093
#comprobar tipo de dato 
print(type(f)) 
[output] <class 'float'> 
```
También podemos cambiar otro tipo a float haciendo uso de float(). Podemos observar como un numero entero como el valor 2, al convertirlo a float, es definido como 2.0. 
```phyton
#creamos una variable decimal con la función float()
b = float(2)
print(b) 
[output] 2.0
```
## String
Los strings o cadenas de caracteres, son un tipo de dato inalterable que permite almacenar series de signos. Para crear una, es preciso incluir el texto entre comillas dobles ".
```phyton
s = "hola, ¿qué tal?"
print(type(s)) 
[output] <class 'str'>
```
## Casting en Python

## List
Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos. Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer elemento.
```phyton
#definimos la lista usando corchetes, separando cada elemento con comas 
factura = ['pan', 'huevos', 100, 1234]
#imprimimos un elemento de la lista
print(factura [0])
[output] pan
```
Es posible crear una lista usando la función list y pasando un objeto iterable.
```phyton
lista=list(“1234”)
print(lista)
[output] ['1', '2', '3', '4']
```
La función len() devuelve la longitud de la lista (su cantidad de elementos).
```phyton
#definimos la lista usando corchetes, separando cada elemento con comas 
factura = ['pan', 'huevos', 100, 1234]
#imprimimos la longitud de la lista
print(len(factura))
[output] 4
```
Además, por medio de los índices, pueden cambiarse los elementos de una lista en el lugar.
```phyton
#definimos la lista usando corchetes, separando cada elemento con comas 
factura = ['pan', 'huevos', 100, 1234]
#cambiamos el valor del elemento  
factura[1] = "carne"
#imprimimos la lista corregida
print(factura)
[output] ['pan', 'carne', 100, 1234]
```
## Tuple
Los tuples son muy similares a las listas, pero con dos diferencias. Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
```phyton
num = (1, 2, 3, 4)
print(num)
[output] (1, 2, 3, 4)
```
## Dictionary
Los diccionarios pueden ser creados colocando una lista separada por coma de pares «key:value» entre {}.
```phyton
#creamos el “key:value” en una línea de código diferente al de la variable
diccionario = {
     "clave1":234,
     "clave2":True,
     "clave3":"Valor 1",
     "clave4":[1,2,3,4]
}
#imprimimos el diccionario junto a cada elemento 
print(diccionario)
[output] {'clave1': 234, 'clave2': True, 'clave3': 'Valor 1', 'clave4': [1, 2, 3, 4]}
```
# Tomando decisiones

## Sentencia if
La sentencia if EXPRESION, significa, Si se cumple la expresión condicional se ejecuta el bloque de sentencias seguidas. Se debe colocar la condición seguida de dos puntos. 
```phyton
n=True
#en este caso la condición dicta que n de be ser verdadera para imprimir un resultado
if n==True:
    print("n es verdadero")
[output] n es verdadero
```
## Ciclo For
El for es un tipo de bucle el cual su número de iteraciones está definido de antemano. En el for existe un iterable que define las veces que se ejecutará el código.
La sentencia for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena de caracteres), en el orden que aparecen en la secuencia.
```phyton
#creamos la variable i para guardar cada valor 
for i in "Hola":
#imprimimos cada valor del for 
    print(i)
[output] H
[output] o
[output] l
[output] a
```
## Ciclo While
El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal.
```phyton
x = 5
while x > 0:
    x -=1
    print(x)
[output] 4,3,2,1,0
```
## Break
La sentencia break nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.
Veamos cómo podemos usar el break con bucles for. El range(5) generaría 5 iteraciones, donde la i valdría de 0 a 4. Sin embargo, en la primera iteración, terminamos el bucle prematuramente.
```phyton
for i in range(5):
    print(i)
#colocamos el break para para el bucle for
    break
# No llega
[output] 0
```
## Continue
El continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar. Es decir, el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.
```phyton
cadena = “hola”
for letra in cadena:
    if letra == h:
        continue
    print(letra)
[output] o
[output] l
[output] a
```
