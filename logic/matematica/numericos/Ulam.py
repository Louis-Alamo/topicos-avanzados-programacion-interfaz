from excepciones.NegativeNumberException import NegativeNumberException

class Ulam():
    def ulam(self, numero):
        if numero < 0:
            raise NegativeNumberException()

        lista = []

        while True:
            anterior = numero

            if (numero % 2 == 0):
                numero = numero /2
                lista.append(f"{anterior} / 2 = {numero}")

                print(f"{anterior} / 2 = {numero}")

            elif (numero % 2 == 1):
                numero = numero * 3 + 1
                lista.append(f"{anterior} * 3 + 1 = {numero}")
                print(f"{anterior} * 3 + 1 = {numero}")

            if numero == 1:

                return lista



