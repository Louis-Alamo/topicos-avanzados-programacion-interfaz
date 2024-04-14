class Palindromo:

    def palindromo(self, palabra):

        palabraInversa = ""

        for i in range(len(palabra)-1, -1, -1):
            palabraInversa += palabra[i]

        if palabra == palabraInversa:
            print(f"La palabra {palabra} es palíndromo")
            return True
        else:
            print(f"La palabra {palabra} no es palíndromo")
            return False

