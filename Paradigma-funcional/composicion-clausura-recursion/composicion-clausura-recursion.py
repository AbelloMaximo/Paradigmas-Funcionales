" Composición, clausura y recursión"

"1) Composicion"
def sumar_tres(x: int) -> int:
    return x + 3

def multiplicar_por_cuatro(x: int) -> int:
    return x * 4

def compuesta(x: int) -> int:
    return multiplicar_por_cuatro(sumar_tres(x))

"2) Clausura"
def crear_multiplicador(factor: int):
    def multiplicar(x: int) -> int:
        return x * factor
    return multiplicar

"3) Recursión (Factorial)"
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Prueba de composición
    entrada = (input("Ingrese un número entero positivo para la composición: "))
    num = int(entrada)
    
    print(f"composicion(({num+3}) * 4): {compuesta(num)}")
    
    multiplicador_personalizado = crear_multiplicador(5)
    print(f"Clausura ({num} multiplicado por 10): {multiplicador_personalizado(10)}")
    
    if num >=0:
        print(f"Recursión (Factorial de {num}): {factorial(num)}")
    else:
        print("El numero no esta definido para numeros negativos")