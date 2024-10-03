# Ejemplo para calcular el area de un triangulo

# Variables de entrada
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))


# Proceso
def calcularAreatriangulo(b, a):
    area = (b * a) / 2
    return area


# Invocar la funcion
resultado = calcularAreatriangulo(base, altura)

# Salida
print(f"El area {base} y la altura {altura} dan una base de:{resultado}")


# Funcion con argumentos predeterminados
def my_function(country="Colombia"):
    print("I am from " + country)


# Invocar la funcion
my_function("Sweden")
my_function("Venezuela")
my_function()


# Funcion con argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: " + args[2])


mostrarEstudiantes("Juan", "David", "Orozco")


# Funcion palabras clave
def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)


mostrarCarros(carro1="BMW", carro3="FERRARI", carro2="FORD")


# Funcion **Kwargs
def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["nombre"])


mostrarCliente(nombre="Tobias", apellido="Refsnes")


# Funcion de paso
def miFuncion():
    pass


# Funciones Integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#Funcion pow(x,y)
num1 = pow(2,3)
print(num1)

#Modeulo de matematicas
import math
num2 = math.sqrt(34)
print(num2)
num3 = math.ceil(7.8)
num4 = math.floor(7.8)
print(num3)
print(num4)
