def calcular_division(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")

# Ejemplo de uso
dividendo = 10
divisor = 2
resultado = calcular_division(dividendo, divisor)
print("El resultado de la división es:", resultado)

