from excepciones.NegativeNumberException import NegativeNumberException
from excepciones.InvalidRangeException import InvalidRangeException
class Primos:

    def formula_primos(self, valorInicial, lista):
        x = valorInicial
        num = self._aplicar_formulas(x)

        if self._comprobar_primo(num):
            print(f"Ciclo1: {x} * {x} - {x} + 41 = {num} : es primo")
            lista.append(f"Ciclo1: {x} * {x} - {x} + 41 = {num} : es primo")
            self.formula_primos(valorInicial=x + 1, lista=lista)
        else:
            print(f"Ciclo1: {x} * {x} - {x} + 41 = {num} : no es primo")
            lista.append(f"Ciclo1: {x} * {x} - {x} + 41 = {num} : no es primo")
            lista.append("Fin")
            print("Fin")

        return lista

    #Criba de haratostenes
    def criba_de_heratostenes(self, cuantosImpares):

        if cuantosImpares < 0:
            raise NegativeNumberException()

        lista_impares = []
        lista_primos = []
        lista = []
        cont = 0
        lista = self._generar_numeros_lista(cuantosImpares, lista, cont, num=3)
        lista2 = lista[:]
        lista_impares = lista[:]

        cont = 0
        while True:
            if cont >= len(lista) or lista[cont] * lista[cont] > lista[-1]:
                break

            lista2 = self._eliminacion(inicio=cont, lista=lista, lista2=lista2, salto=lista[cont])
            cont += 1

        self._mostrar_lista(lista2)

        return lista_impares, lista2

    #Serie mas larga de numeros no primos
    def serie_numeros_no_primos(self, limiteInferior, limiteSuperior):

        if limiteInferior < 0 or limiteSuperior < 0:
            raise NegativeNumberException

        if limiteInferior > limiteSuperior:
            raise InvalidRangeException()

        lista_numeros = []
        for num in range(limiteInferior, limiteSuperior + 1):
            lista_numeros.append(num)

        serie_actual = []
        mejor_serie = []
        for num in lista_numeros:
            if not self._comprobar_primo(num):
                serie_actual.append(num)
            else:
                if len(serie_actual) > len(mejor_serie):
                    mejor_serie = serie_actual
                serie_actual = []

        if len(serie_actual) > len(mejor_serie):
            mejor_serie = serie_actual

        print(mejor_serie)



        return lista_numeros, mejor_serie
    def generar_numeros_primos_rango(self, limiteInferior, limiteSuperior):

        if limiteInferior < 0 or limiteSuperior < 0:
            raise NegativeNumberException

        if limiteInferior > limiteSuperior:
            raise InvalidRangeException()


        lista = []
        for num in range(limiteInferior, limiteSuperior + 1):
            if self._comprobar_primo(num):
                lista.append(num)
        return lista





            
    def _mostrar_lista(self, lista2):
        for i in lista2:
            if i != 0:
                print(i, end=",")

    def _eliminacion(self, inicio, lista, lista2, salto):
        for i in range(inicio + salto, len(lista), salto):
            lista2[i] = 0
        return lista2

    def _generar_numeros_lista(self, cuantosImpares, lista, cont, num):
        if cont == cuantosImpares:
            return lista
        else:
            lista.append(num)
            return self._generar_numeros_lista(cuantosImpares, lista, cont=cont + 1, num=num + 2)
    def _comprobar_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def _aplicar_formulas(self, x):
        return ((x*x)-x)+41

