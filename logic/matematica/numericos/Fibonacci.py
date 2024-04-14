from excepciones.NegativeNumberException import NegativeNumberException

class Fibonacci():

    def fibonacci(self, semilla1, semilla2, cantidad):

        if semilla1 < 0 or semilla2 < 0 or cantidad < 0:
            raise NegativeNumberException()

        lista = []
        lista.append(f"{semilla1},")
        lista.append(f"{semilla2}")
        print(f"{semilla1},{semilla2}", end="")

        for i in range(cantidad - 2):  
            siguiente = semilla1 + semilla2
            print(f",{siguiente}", end="")
            lista.append(f",{siguiente}")
            semilla1, semilla2 = semilla2, siguiente

        return lista



