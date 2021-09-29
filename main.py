# Titulo y Espaciado
def printMio(que):
    print()
    print(que)
    print()

# Comentario una linea

"""
Comentario multilinea
"""

#--------------------------------------------------------------------------------------------------
# Hola Mondo

print()
print("Hola Mundo")

#--------------------------------------------------------------------------------------------------
# Funciones nativas: print() - len() - input() - type()
printMio("Funciones nativas:")

print("Hola", end=" ")  # end="" Elimina salto de linea
print("Hola")

cantLetras = len("Emanuel")
print(f"Emanuel tiene {cantLetras} letras")

varIn =  input("Escrive algo: ")  # Entrada por consola
print(f"Escribiste: {varIn}")

print(type(cantLetras))  # Tipo de dato

#--------------------------------------------------------------------------------------------------
# Variables y tipos de datos
# strings, numeros y booleans --- na más

texto = "Lo que sea"
textoLargo = """Esto es
             un texto
             muy largo"""

numero = 5
numeroDecimal = 5.5  # solo float
numeroComplejo = 3 + 2j  # a saber que es esto

buleano = True

#--------------------------------------------------------------------------------------------------
# Operadores

# Aritmeticos
# suma +   resta -   multi *   div /   modulo %   exponente **   divEntera //

# Comparacion
# igual ==   distinto !=   mayQue >   menQue <   mayIguQue >=   menIguQue <=

# Logicos
# tal cual: and   or   not

# Asignacion
#   =    +=    -=    *=    /=    %=    **=    //=

# Especiales (conprobar si un valor se encuentra en un conjunto)
# is  -  is not  -  in  -  not in

#--------------------------------------------------------------------------------------------------
# Listas - pueden tener elementos de DISTINTOS TIPOS
printMio("Listas:")

personas = ["Ema", "Victor", "Pepe", "Clari"]

print(personas[0])
print(personas[1:3]) # inprime de 1º al 2º-1  -  [0,2)
print(personas[:2]) # desde el principio hasta el num -1; [2:] desde el num -1 hasta el ultimo

personas.append("LocaFea")
personas.insert(2,"Rocco")  # Inserta en el "2" el elemento
personas.extend(["Ana","Lucia"])

personas.remove("LocaFea")
personas.pop() # elimina el ultimo elemento

# listaUnoMasDos = listaUno + listaDos
# repetidaX3 = [1,2,3] * 3

index = personas.index("Ema")  # da la posicion de primer elemento que coinsida
presente = "Ema" in personas  # True o Falso

print(personas)

#--------------------------------------------------------------------------------------------------
# Tuplas INVESTIGAR
tupla = ("Ema", "Victor", "Pepe", "Clari")

#--------------------------------------------------------------------------------------------------
# Diccionario INVESTIGAR
diccionario = {"num1":1,"num2":2,"num3":3,"num4":4,"num5":5}

#--------------------------------------------------------------------------------------------------
# Concatenacion piola
printMio("Concatenacion piola:")

print(f"{texto} {numero}")

#--------------------------------------------------------------------------------------------------
# Conversion

numTxt = str(numero)
txtANum = int("5")
txtANumDec = float("5.5") # Con "." no con ","
bool1 = bool(0) # 0 False | N '-' 0 '+' Frue
bool2 = bool("") # "" False | "Algo" Frue
    # False y True van con la 1º en mayuscula

#--------------------------------------------------------------------------------------------------
# Condicionales  -  switch NO EXISTE ACA
printMio("Condicioneles:")

altura = 177

if altura >= 180:  # Puede ir entre ()
    print("Sos una persona alta!") # Hay que indentar si o si, gerarquia de tabulaciones
elif altura <= 150:
    print ("Sos un petizo!")
else:
    print("Tu altura es normal!")

#--------------------------------------------------------------------------------------------------
# Funciones
printMio("Fuciones:")

  # Las variables se manejan POR REFERENCIA, cuado declaro numA1 y se lo paso a la funcion
  # con el nombre de numB1, le digo la direccion en memoria, no el valor, por eso
  # si modifico numB1 dentro de la funcion, se modifica numA1

numa1 = 5
numa2 = 6

def suma(numb1, numb2): # Ojo con las tabulaciones
    numb1 = 6
    return numb1 + numb2

print(suma(numa1,numa2))   # Esto es igual a 12; no 11 que seriacon el paso de parametro POR VALOR

#--------------------------------------------------------------------------------------------------
# Bubles
printMio("Bucles:")

    # Determinados

for persona in personas:  # foreach en C#, pero no igual
    print(persona)

    # Si in es un string, ejecuta la cantidad de caracteres

  # Con 1 argumento = cantidad de iteraciones, incremental
  # Con 2 argumentos va de 1º al 2º
  # Con 3 argumentos va de 1º al 2º de "2" en "2"
for i in range(4,10,2): 
    print(f"Hola {i}")  # Con "f" hace un convert sin decirselo

    # Indeterminados

prueva = True
acu = 0

    # while prueva == True and nose == nose:
while prueva == True:  # MIENTRAS SEA TRUE
    prueva = bool(input("Presione Enter para finalizar u otra tecla para iterar:"))
    acu += 1  # No hay "++"
print(f"Presionaste {acu} tecla")

# do while, no tiene!! hay que hacerlo con codigo 
# Ejecutas lo que hay en el bucle que queres que se ejecute una vez, arriva de la declarecion y despues en el bucle

#--------------------------------------------------------------------------------------------------
# try except (try catch)
printMio("try except (try catch):")

try:  
    texto + numero
except:
    print("No se puede calcular")

#--------------------------------------------------------------------------------------------------
# Continue (salta la iteracion), pass (devuelve null) y else (igual que en if)
printMio("Continue, pass y else:")

for letra in "Python": 
    if letra == "h":
        continue   # Salta lo que hay abajo para volver a iterar
    print(letra, end="")
print()

  # pass para hacer una clase o funcion null y cortar bucles "while True:" con "ctrl + C"
  # "ctrl + C" rompe bucles infinitos!

  # else con bubles, se ejecuta cuando terminen las iteraciones
  # no se ejecuta cuando se interrumpe con break

#--------------------------------------------------------------------------------------------------
# Clase
printMio("Clases:")

  # No hay sobrecarga
  # La sobrecarga se fabrica, es el mismo metodo o un metodo que llama a otros 2 o 3 o ... "sobrecargas"; ejecuta segun las condiciones

class Padre():
    def __init__(self):
        self.propiedadPadre = "Padre"
    

class Clase(Padre):
    def __init__(self):  # constructor
        self.__propiedad = ""  # __ es: private y debe ir en todas las menciones del atributo en la clase __var es una variable y solo var es otra

    def __metodoEncapsulado(self):  # metodo encapsulado
        self.__propiedad = "Escrive con el metodo encapsulado"

    def metodo(self): # self = this hace referencia a la instancia de la clase, recive por parametro implicitamente el objeto
        self.__metodoEncapsulado()
        print(f"Imprime {self.__propiedad}")

    def metodoConParametro(self,texto): # metodo con parametros
        print(f"Imprime {texto}")

    # no se pueden ejecutar los metodos en el cuerpo de la clase
    # el metodo: pertenece a la clase
    # la funcion: no pertenece una clase

clase = Clase() # en la instanciacion, si el padre tiene parametros, se ponen en el constrictor del hijo
#clase.propiedad = "Algo"
clase.metodo()
clase.metodoConParametro("Otra cosa")
clase.propiedadPadre = "Provando 1, 2, 3"


#--------------------------------------------------------------------------------------------------
# import Clase
# Lamado de Clases (Math)
printMio("Importar clase:")

import math

cuadrado = math.sqrt(2)  # Rais cuadrada de "(2)"
print(f"La raiz cuadrada de 2 es: {cuadrado}")




print()




#            * * * * *            * * * * * * *         * * * * *
#            *         *                *               *         *
#            *          *               *               *          *
#            *          *               *               *          *
#            *         *                *               *         *
#            * * * * *                  *               * * * * * 
#            *                          *               *
#            *                          *               *
#            *                          *               *
#            *                    * * * * * * *         *











