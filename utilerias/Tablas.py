from tabulate import tabulate

class Tablas:

    def __init__(self, titulo):
        self.tituloTabla = titulo
        self.valoresColumna = []
        self.titulos = []

    def agregar_columna(self, titulo, datos):
        self.titulos.append(titulo)
        self.valoresColumna.append(datos)

    def obtener_columna(self, indice):
        return self.valoresColumna[indice]

    def imprimir_tabla(self):
        print(self.tituloTabla)
        print("--------------------------------")
        # Transponer los datos de la tabla
        tabla_transpuesta = list(map(list, zip(*self.valoresColumna)))
        # Imprimir la tabla con tabulate
        print(tabulate(tabla_transpuesta, headers=self.titulos))
        print("\n")






