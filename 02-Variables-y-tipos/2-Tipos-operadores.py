# Operadores

# Operadores numéricos
"""
Símbolo     Significado     Ejemplo         Resultado
+           Suma            a = 10 + 5      a es 15 
-           Resta           a = 12 - 7      a es 5 
-           Negación        a = -5          a es -5 
*           Multiplicación  a = 7 * 5       a es 35 
**          Exponente       a = 2 ** 3      a es 8 
/           División        a = 12.5 / 2    a es 6.25 
//          División entera a = 12.5 / 2    a es 6.0 
%           Módulo          a = 27 % 4      a es 3
"""

"""
PEP 8: operadores
Siempre colocar un espacio en blanco, antes y después de un
operado
"""

# Operaciones de asignación
"""
num1 = 5
num1 += 3  # Resultado es num1 + 3
print(f"Valor de num1 = {num1}")
num1 -= 2  # Resultado es num1 - 2
print(f"Valor de num1 = {num1}")
"""

# Operadores relacionales

"""
Símbolo     Significado         Ejemplo             Resultado
==          Igual que           5 == 7              Falso 
!=          Distinto que        rojo != verde       Verdadero
<           Menor que           8 < 12              Verdadero
>           Mayor que           12 > 7              Falso
<=          Menor o igual que   12 <= 12            Verdadero
>=          Mayor o igual que   14 >= 12            Verdadero
"""

# Operadores lógicos

"""
Operador        Ejemplo                 Resultado*
and (y)         5 == 7 and 7 < 12       0 y 1       Falso
                9 < 12 and 12 > 7       1 y 1       Verdadero
                9 < 12 and 12 > 15      1 y 0       Falso
or (o)          12 == 12 or 15 < 7      1 o 0       Verdadero
                7 > 5 or 9 < 12         1 o 1       Verdadero
xor             4 == 4 ^ (xor) 9 > 3    1 o 1       Falso
(o excluyente)  4 == 4 ^ (xor) 9 < 3    1 o 0       Verdadero       
"""

resul = (7 == 7) and (7 < 12)


resul = (4 == 5)  ^  (9 < 3)
print (resul)

"""
Operador
Función
Ejemplos
Resultado
“In”
El operador In (en) devuelve True si un elemento se encuentra dentro de otro.	a = [3, 4] 3 in a	True
Porque “3” se encuentra en “a”
“Not in”
El operador Not In (en) devuelve True si un elemento no se encuentra dentro de otro.	a = [3, 4] 5 in a	True
Porque “5” no se encuentra en “a”
“Is”
El operador “Is” (es) devuelve True si los elementos son exactamente iguales.	x = 10
y = 10
x is y	True
Porque ambas variables tienen el mismo valor, son iguales.
“Is Not”
El operador “is not”(no es) devuelve true si los elementos no son exactamente iguales.	x = 10
y = 111
x is not y True
Porque estas variables no tienen el mismo valor, por ende son diferentes.
"""
x = 10
y = 0


print (f"X no esta en Y: {x is not y}")