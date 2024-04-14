class IntercambioLetra():

    def intercambio_letra_elegida(self, letra, letra_nueva, texto):
        print(f"Texto antiguo: " + texto)

        nuevo_texto = ""  # Inicializamos una cadena vacía para construir el nuevo texto

        for char in texto:
            if char == letra:
                nuevo_texto += letra_nueva
            else:
                nuevo_texto += char
        
        print(f"Texto nuevo: " + nuevo_texto)
    
    def intercambio_letra_vocales(self, letraNueva, texto):
        print(f"Texto antiguo: "  + texto)
        nuevoTexto = ""

        for char in texto: 
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                nuevoTexto += letraNueva
            else:
                nuevoTexto += char
            
        print("Texto nuevo: " + nuevoTexto)
        return nuevoTexto


