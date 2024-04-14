import random

def llenar_lista_aleatorios(lista, cantidad, limite_inferior=1, limite_superior=1000):
    """
    Llena una lista con números aleatorios.

    Args:
        lista (list): La lista a llenar.
        cantidad (int): La cantidad de números aleatorios a generar.
        limite_inferior (int, optional): El límite inferior para los números aleatorios. Por defecto es 1.
        limite_superior (int, optional): El límite superior para los números aleatorios. Por defecto es 1000.

    Returns:
        list: La lista llena con números aleatorios.
    """
    for i in range(cantidad):
        lista.append(random.randint(limite_inferior, limite_superior))

    return lista

def ordenar_burbuja(lista):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento de burbuja.

    Args:
        lista (list): La lista a ordenar.

    Returns:
        list: La lista ordenada.
    """
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def mezclar_listas(lista1, lista2):
    """
    Mezcla dos listas ordenadas en una nueva lista ordenada.

    Args:
        lista1 (list): La primera lista ordenada.
        lista2 (list): La segunda lista ordenada.

    Returns:
        list: La lista resultante de mezclar las dos listas de entrada.
    """
    lista_final = []

    contLista1 = 0
    contLista2 = 0

    while True:

        if lista1[contLista1] < lista2[contLista2]:
            lista_final.append(lista1[contLista1])
            contLista1 += 1
        else:
            lista_final.append(lista2[contLista2])
            contLista2 += 1

        if contLista1 == len(lista1):

            for i in range(contLista2, len(lista2)):
                lista_final.append(lista2[i])
            break

        if contLista2 == len(lista2):
            for i in range(contLista1, len(lista1)):
                lista_final.append(lista1[i])
            break

    return lista_final