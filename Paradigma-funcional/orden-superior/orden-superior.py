"funciones como valores y de orden superior"

def multiplicar_por_dos(x: int) -> int:
    return x * 2

def elevar_al_cuadrado(x: int) -> int:
    return x ** 2

#Funcion de orden superior
def aplicar_operacion(func, lista: list) -> list:
    return [func(x) for x in lista]

if __name__ == "__main__":
    entrada=input("Ingrese un numero para operar: ")
    num=int(entrada)
    
    #Creamos una base de datos pequeña con ese numero y otos
    datos=[num, num+1, num+2]
    print(f"Lista base generada: {datos}")
    
    print("Aplicando elementos con orden superior:", aplicar_operacion(multiplicar_por_dos, datos))
    print("Elevando el cuadrado con lambda:", aplicar_operacion(lambda x: x**2, datos))