# %% Ejercicio 1
#Diseña un programa que convierta dólares americanos a pesos mexicanos, euros, libras esterlinas, yuanes 
#y rublos utilizando una tasa de cambio fija. Muestre la tasa de cambio e imprima los cinco resultados.

#Conversión de monedas
#Defino las siguientes variables, donde el valor asignado es el equivalente a un dólar americano para cada divisa, es decir el equivalente
#a un dólar en pesos mexicanos, euros, libra esterlina, yuanes y rublos, respectivamente.

usd_mx=18.42
usd_eur=0.85
usd_gbp=0.74
usd_cny=7.12
usd_rub=82.55

usd_cantidad=float(input("Ingrese la cantidad de dólares a convertir: "))

if usd_cantidad>0:
    print('La tasa de cambio del dólar americano a pesos mexicanos es de 1 USD=18.24 MX')
    print('La tasa de cambio del dólar americano a euros es de 1 USD=0.85 EUR')
    print('La tasa de cambio del dólar americano a libra esterlina es de 1 USD=0.74 GBP')
    print('La tasa de cambio del dólar americano a yuanes es de 1 USD=7.12 CNY')
    print('La tasa de cambio del dólar americano a rublos es de 1 USD=82.55 RUB')
    total_mx=usd_cantidad*usd_mx #Se hace la conversión de dolares a cada una de las divisas, multiplicando las tasas de cambio por la cantidad de dólares ingresada por el usuario
    total_eur=usd_cantidad*usd_eur
    total_gbp=usd_cantidad*usd_gbp
    total_cny=usd_cantidad*usd_cny
    total_rub=usd_cantidad*usd_rub
    print(usd_cantidad,'dólares equivalen a',round(total_mx,2),'pesos mexicanos')
    print(usd_cantidad,'dólares equivalen a',round(total_eur,2),'euros')
    print(usd_cantidad,'dólares equivalen a',round(total_gbp,2),'libras esterlinas')
    print(usd_cantidad,'dólares equivalen a',round(total_cny,2),'yuanes')
    print(usd_cantidad,'dólares equivalen a',round(total_rub,2),'rublos')
else:
    print('Ingrese un número válido') #Si el usuario ingresó una cantidad negativa, se le pide que ingrese un número válido


# %% Ejercicio 2
#Crea un programa que solicite al usuario dos números y realice las operaciones básicas como suma, resta, multiplicación, división, potenciación y raíz cuadrada. Muestra los resultados usando variables.

#Defino dos variables a y b, las cuales se le solicitarán al usuario con un input

import math #Importando la librería math para utilizar la raiz cuadrada

a=float(input('Ingrese un primer número: '))
b=float(input('Ingrese un segundo número: '))

#Defino las variables para cada una de las operaciones solicitadas

suma=a+b
resta=a-b
mult=a*b
div=a/b
potencia=a**b
raiz_a=math.sqrt(a)
raiz_b=math.sqrt(b)

#Imprimo en pantalla los resultados de cada operación definida en las variables para los valores dados por el usuario

print('La suma de',a,'y',b,'es',round(suma,3))
print('La resta de',a,'y',b,'es',round(resta,3))
print('La multiplicación entre',a, 'y' ,b, 'es',round(mult,3))
print('La división de',a,'entre',b,'es',round(div,3))
print('El número',a,'elevado a la potencia',b,'es',round(potencia,3))
print('Las raices cuadradas de',a,'y',b,'son',round(raiz_a,3),'y',round(raiz_b,3),'respectivamente')

# %% Ejercicio 3 
# Desarrolla un programa que calcule el precio final de un producto después de aplicar un descuento. El usuario debe ingresar el precio original y el porcentaje de descuento. Utiliza variables para almacenar los valores.

precio=int(input('Ingrese el precio del producto: '))
descuento=int(input('Ingrese el descuento del producto: '))

if precio>0:
    precio_final=precio*(100-descuento)/100
    print(f"El precio final del producto es ${precio_final}")
else:
    print('Ingrese un precio válido')

# %% Ejercicio 4
#Conversión de coordenadas y localización geográfica. Para cada uno de los siguientes pares de coordenadas (latitud, longitud), realiza lo siguiente usando solo variables (sin funciones definidas por ti, sin ciclos):
# a).- Guarda los valores de grados, minutos y segundos en variables separadas (por latitud y por longitud).
# b).- Convierte cada coordenada a grados decimales mediante la fórmula: decimal=grados+minutos/60+segundos/3600.
# Imprime la latitud y longitud con su valor decimal. Redondee los valores a 3 decimales (si aplica).
# Busca en la literatura (o en línea) qué lugar emblemático corresponde aproximadamente a esas coordenadas.

#Declaramos las variables de grado, minuto y segundo para la latitud de las tres coordenadas

grado_lat1=40
min_lat1=41
seg_lat1=21

grado_lat2=48
min_lat2=51
seg_lat2=12

grado_lat3=34
min_lat3=3
seg_lat3=8

#Declaramos las variables de grado, minuto y segundo para la longitud de las tres coordenadas

grado_long1=74
min_long1=2
seg_long1=40

grado_long2=2
min_long2=20
seg_long2=55

grado_long3=151
min_long3=12
seg_long3=33

#Mediante la fórmula dada, convertimos cada una de las coordenadas a grados decimales

decimal_lat1=grado_lat1+(min_lat1/60)+(seg_lat1/3600)
decimal_long1=-(grado_long1+(min_long1/60)+(seg_long1/3600))

decimal_lat2=grado_lat2+(min_lat2/60)+(seg_lat2/3600)
decimal_long2=grado_long2+(min_long2/60)+(seg_long2/3600)

decimal_lat3=-(grado_lat3+(min_lat3/60)+(seg_lat3/3600))
decimal_long3=grado_long3+(min_long3/60)+(seg_long3/3600)

#Imprimimos en pantalla las coordenadas en grados decimales con las variables obtenidas anteriormente y los lugares aproximados a dichas coordenadas

print(f"La coordenada 1 en grados decimales es ({round(decimal_lat1,3)},{round(decimal_long1,3)})")
print(f"El lugar aproximado para la coordenada 1 es la Estatua de la Libertad, ubicada en Nueva York, Estados Unidos")
print(f"La coordenada 2 en grados decimales es ({round(decimal_lat2,3)},{round(decimal_long2,3)})")
print(f"El lugar aproximado para la coordenada 2 es la Catedral de Notre Dame, ubicada en Paris, Francia")
print(f"La coordenada 3 en grados decimales es ({round(decimal_lat3,3)},{round(decimal_long3,3)})")
print(f"El lugar para la coordenada 3 se encuentra aproximadamente a 1 km de la costa de la reserva acuática Boat Harbor y de Mushroom Rock, ubicado en Kurnell, Australia")

# %% Ejercicio 5 
# Un objeto de masa m=2 kg se encuentra a una altura h=10 cm y tiene una velocidad de v=3 m/s. Calcular:
#a) La energía cinética (Ec),
#b) La energía potencial gravitacional (Ep),
#c) La energía mecánica total (Em).
# Considere g=9.8m/s^2. Revise las unidades.

#Declaramos las variables para la masa, la altura, la velocidad y la gravedad

m=2
h=10*(1/100)
vel=3
g=9.8

#Fórmula para la energía cinética y energía potencial gravitacional

e_cin=(m*vel**2)/2
e_pot=m*h*g

#Fórmula para la energía mecánica total

e_mec=e_cin+e_pot

print(f"La energía cinética es {e_cin} kg*m^2/s^2")
print(f"La energía potencial es {round(e_pot,2)} kg*m^2/s^2")
print(f"La energía mecánica total es {e_mec} kg*m^2/s^2")

# %% Ejercicio 6 
# Escribe un programa que pida un número entero y determine si es par o impar utilizando la sentencia if-elif-else. Si el valor ingresado no es un entero válido, el programa debe indicarlo y que vuelva a ejecutar el programa.

#Se le pide al usuario que ingrese un número entero

num=float(input("Ingrese un número entero: "))

#Con la operación de módulo se determina si el número es par o impar

if num % 2==0 : #Se analiza el caso en el que el módulo es cero, es decir, el número es par
    print("El número ingresado es par")
elif num % 2==1: #Se analiza el caso en el que el módulo es 1, es decir, el número es impar
    print("El número ingresado es impar")
else: #Si el usuario ingresa un número decimal, entonces se le pide que ingrese un número válido, es decir, un entero
    print("Ingrese un número válido")


# %% Ejercicio 7 Solicite al usuario que ingrese los valores de los lados de un triángulo (enteros positivos) y realice lo siguiente:
# a).- Valide que formen un triángulo (desigualdad triangular).
# b).- Si forman un triángulo, indica si es equilátero, isosceles o escaleno.

a=int(input("Ingrese una longitud del lado de un triángulo: "))
b=int(input("Ingrese la segunda longitud del lado de un triángulo: "))
c=int(input("Ingrese la tercera longitud del lado de un triángulo: "))

if a+b>c and a+c>b and b+c>a: #primer if para determinar que sí es un triángulo a partir de la desigualdad triangular
    print("Los valores ingresados forman un triángulo")

    if a==b and b==c: #If anidado, si sí es un triángulo, analizamos que si los lados son iguales entonces es equilátero
        print("El triángulo es equilátero") 
    elif a!=b and a!=c and b!=c: #Si no es equilátero y todos los lados son distintos, entonces es escaleno
        print("El triángulo es escaleno")
    else: #Si no es escaleno ni equilátero, entonces es isósceles
        print("El triángulo es isósceles")
else: #Si en el primer if se determina que no es triángulo, entonces se imprime en pantalla que no lo es
    print("Los valores ingresados no forman un triángulo")

# %% Ejercicio 8 Crea un script en Python que determine cuál de tres números introducidos por el usuario es el mayor, usando sentencias IF anidadas o múltiples ELIF

#Declaramos las variables para cada número que introducirá el usuario.

a=float(input("Ingrese un número: "))
b=float(input("Ingrese un segundo número: "))
c=float(input("Ingrese un tercer número: "))

if (a>b and a>c): #Analizamos todos los casos en los que a es mayor que b y c
    print(f"{a} es mayor que {b} y {c}")
elif (b>a and b>c): #Analizamos todos los casos en los que b es mayor que a y c
    print(f"{b} es mayor que {a} y {c}")
elif (c>a and c>b) : #Analizamos todos los casos en los que c es mayor que a y b
    print(f"{c} es mayor que {a} y {b}")
else:
    print("Ingrese números distintos entre sí") #Si no se cumplen los tres casos anteriores, entonces hay al menos dos que son iguales

# %% Ejercicio 9 Programe un script en Python que determine si dos rectas dadas por las ecuaciones y1=m1x + b1 y y2=m2x+b2 se intersectan, son paralelas o coincidentes. Utilice estructuras de control (IF - ELSE) para manejar los diferentes casos.

#Declaramos las variables para la pendiente y la ordenada al origen, las cuales se le solicitarán al usuario

m1=int(input("Ingrese la pendiente de la recta L1: "))
b1=int(input("Ingrese la ordenada al origen de la recta L1: "))
m2=int(input("Ingrese la pendiente de la recta L2: "))
b2=int(input("Ingrese la ordenada al origen de la recta L2"))

if m1==m2 and b1==b2: #Analizamos que si la pendiente y la ordenada al origen son iguales, se trata de la misma recta
    print("Las rectas L1 y L2 son coincidentes, es decir, comparten todos sus puntos")
elif m1==m2 and b1!=b2: #Analizamos que si las pendientes son iguales pero las ordenadas al origen no, entonces son paralelas
    print("Las rectas L1 y L2 son paralelas")
else: #Si no pasan los dos primeros casos, entonces las rectas son secantes
    print("Las rectas L1 y L2 se intersecan en un solo punto")


# %% Ejercicio 10 Escriba un programa que solicite al usuario un año y que el programa indique si es bisiesto o no. Recuerde, los años bisiestos son múltiplos de 4, no es el caso para los múltiplos de 100, pero si para los múltiplos de 400.

year=int(input("Ingrese un año cualquiera en la era actual (d.C):"))

if year<0:
    print("Ingrese un año válido (no negativo)")
elif year>=0 and year%4==0 and year%100!=0: #Si el año dado por el usuario es múltiplo de 4 pero no de 100, entonces es bisiesto
    print(f"El año {year} es bisiesto")
elif year>=0 and year%4==0 and year%100==0 and year%400==0: #Si el año es múltiplo de 4 y de 100, si es múltiplo de 400, es bisiesto
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto") #Si no se cumplen los dos casos anteriores, entonces el año es no bisiesto
