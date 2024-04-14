from logic.evaluacion.OperacionesListas import llenar_lista_aleatorios, ordenar_burbuja, mezclar_listas

class MergeSort:
    """
    Clase que representa el algoritmo de ordenamiento Merge Sort.

    Args:
        cantidad1 (int): La cantidad de elementos en la primera lista.
        cantidad2 (int): La cantidad de elementos en la segunda lista.

    Attributes:
        lista1 (list): La primera lista de números aleatorios.
        lista2 (list): La segunda lista de números aleatorios.
        cantidad1 (int): La cantidad de elementos en la primera lista.
        cantidad2 (int): La cantidad de elementos en la segunda lista.
        lista_final (list): La lista final que resulta de mezclar y ordenar las dos listas.
    """

    def __init__(self, cantidad1, cantidad2):
        """
        Inicializa una nueva instancia de MergeSort.

        Args:
            cantidad1 (int): La cantidad de elementos en la primera lista.
            cantidad2 (int): La cantidad de elementos en la segunda lista.
        """
        self.lista1 = []
        self.lista2 = []
        self.cantidad1 = cantidad1
        self.cantidad2 = cantidad2
        self.lista_final = []

    def inicio_algoritmo(self):
        """
        Inicia el algoritmo de ordenamiento Merge Sort.
        Llena las listas con números aleatorios, las ordena y luego las mezcla.
        """
        self.lista1 = llenar_lista_aleatorios(self.lista1, self.cantidad1)
        self.lista2 = llenar_lista_aleatorios(self.lista2, self.cantidad2)
        self.lista1_ordenada = ordenar_burbuja(self.lista1.copy())
        self.lista2_ordenada = ordenar_burbuja(self.lista2.copy())
        self.lista_final = mezclar_listas(self.lista1_ordenada, self.lista2_ordenada)

    def get_lista1(self):
        """
        Devuelve la primera lista de números aleatorios.

        Returns:
            list: La primera lista de números aleatorios.
        """
        return self.lista1

    def get_lista2(self):
        """
        Devuelve la segunda lista de números aleatorios.

        Returns:
            list: La segunda lista de números aleatorios.
        """
        return self.lista2

    def get_lista1_ordenada(self):
        """
        Devuelve la primera lista de números aleatorios ordenada.

        Returns:
            list: La primera lista de números aleatorios ordenada.
        """
        return self.lista1_ordenada

    def get_lista2_ordenada(self):
        """
        Devuelve la segunda lista de números aleatorios ordenada.

        Returns:
            list: La segunda lista de números aleatorios ordenada.
        """
        return self.lista2_ordenada

    def get_lista_final(self):
        """
        Devuelve la lista final que resulta de mezclar y ordenar las dos listas.

        Returns:
            list: La lista final que resulta de mezclar y ordenar las dos listas.
        """
        return self.lista_final