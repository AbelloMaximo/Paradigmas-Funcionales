"Funciones puras, inmutabilidad y efectos secundarios"

# Funcion pura
def sumar_cinco_puro(x: int) -> int:
    return x + 5

if __name__ == "__main__":
    entrada = input("Ingresa un numero entero")
    numero = int(entrada)
    
    print(f"aplicando funcion pura (sumar 5): {sumar_cinco_puro(numero)}")
    
    # Inmutabilidad con tuplas
    tupla_original = (1, 2, 3)
    tupla_nueva = tupla_original + (numero,)
    
    print(f"Tupla original (inmutable): {tupla_original}")
    print(f"Tupla nueva con tu numero agregado: {tupla_nueva}")