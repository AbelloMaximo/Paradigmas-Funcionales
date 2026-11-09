# Evaluación estricta y evaluación perezosa

if __name__ == "__main__":
    
    entrada = input("¿Cuantos elementos perezosos quire agregar?: ")
    cantidad = int(entrada)
    
    # Genrador perezoso con yield
    def generador_cubos(n: int):
        for i in range(n):
            yield i ** 3
            
    lazy_nums = generador_cubos(cantidad)
    print("Objeto generador creado en memoria sin calcular todo de golpe.")
    
    #Pedir elementos bajo demanda iterativa
    while True:
        opcion = input("¿Quieres calcular el siguiente valor con 'next()'? (s/n):")
        if opcion == 's':
            try:
                print("Siguiente valor:", next(lazy_nums))
            except StopIteration:
                print("¡Ya no quedan mas elementos en el generador!")
                break
        else:
            print("Saliendo del generador perezoso...")
            break