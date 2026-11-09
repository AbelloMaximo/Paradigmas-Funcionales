"Coincidencia de patrones y tipos algebraicos"

from dataclasses import dataclass
from typing import Union

@dataclass
class cuadrado:
    lado: float
    
@dataclass
class circulo:
    radio: float
    
Figura = Union[cuadrado, circulo]

def calcular_area(figura: Figura) -> float:
    match figura:
        case cuadrado(l):
            return l ** 2
        case circulo(r):
            return 3.14159 * (r ** 2)
        case _:
            raise ValueError("Figura no reconocida")
        
if __name__ == "__main__":
    entrada = input("Ingrese una medida (radio o lado) para calcular el área: ")
    medida = float(entrada)
    
tipo = input("¿Es un 'circulo' o un 'cuadrado'? ").strip().lower()

if tipo == "circulo":
    fig = circulo(radio=medida)
elif tipo == "cuadrado":
    fig = cuadrado(lado=medida)
else:
    fig = None
    print("Figura no reconocida por defecto. Usando cuadrado por seguridad.")
    fig = cuadrado(lado=medida)
    
print(f"El área calculada mediante Pattern Matching es: {calcular_area(fig)}")