"Map, filter y fold (reduce) en Python"

from functools import reduce

if __name__ == "__main__":
    entrada = input("Ingrese un numero limite para generar una lista de numeros ej(6): ")
    limite = int(entrada)
    
    nums = list(range(1, limite+1))
    print(f"Lista generada: {nums}")

# Map
cuadrados = list(map(lambda x: x**2, nums))
print(f"Map (al cuadrado):", cuadrados)

#Filter
impares = list(filter(lambda x: x % 2 != 0 , nums))
print(f"Filter (solo numeros imapres):", impares)

#Fold (reduce)
multiplicacion_total = reduce(lambda acumulador, x: acumulador * x, nums, 1)
print(f"Fold (multiplicacion acumulable de la lista):", multiplicacion_total)