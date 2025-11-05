##Elabore una función que dado un número ingresado calcule el cuadrado de un número si este es impar, o el cubo
#  de un número si este es par. Por ejemplo, para 4 tu programa debe entregar 64, y para 3 debe entregar 9.

def calcular_numero(numero):
    if numero % 2 == 0:
        resultado = numero ** 3
    else:
        resultado = numero ** 2
    return resultado

# Programa principal
num = int(input("Ingrese un número: "))
print("El resultado es:", calcular_numero(num))
