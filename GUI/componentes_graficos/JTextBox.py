from customtkinter import CTkTextbox
from tkinter import END
from tabulate import tabulate
from utilerias.Tablas import Tablas


class JTextBox(CTkTextbox):
    """
    Clase que representa un área de texto personalizada utilizando la biblioteca customtkinter.

    Args:
        master: El widget padre al que pertenece este área de texto.

    Attributes:
        master: El widget padre al que pertenece este área de texto.

    """

    def __init__(self, master):
        """
        Inicializa un nuevo JTextBox.

        Args:
            master: El widget padre al que pertenece este área de texto.

        """
        super().__init__(master=master)

        # Configura las propiedades del área de texto
        self.configure(font=("Arial", 15),        # Fuente del texto en el área de texto
                       fg_color="#e0eef9",        # Color del texto en el área de texto
                       corner_radius=5,           # Radio de las esquinas del área de texto
                       border_color="#77b4e3",    # Color del borde del área de texto
                       text_color="#000000",      # Color del texto en el área de texto
                       border_width=2             # Ancho del borde del área de texto
                       )

    def eliminar_texto(self):
        """
        Elimina todo el texto presente en el área de texto.
        """
        self.delete(1.0, END)

    def insertar_texto_lista(self, lista):
        """
        Inserta una lista de elementos como texto en el área de texto.

        Args:
            lista (list): La lista de elementos que se insertarán en el área de texto.
        """
        self.configure(state="normal")

        for elemento in lista:
            self.insert(END, str(elemento) + '\n')
        self.configure(state="disable")

    def insertar_texto(self, texto):
        """
        Inserta el texto especificado en el área de texto, añadiéndolo al final del texto existente.

        Args:
            texto (str): El texto que se insertará en el área de texto.
        """
        self.configure(state="normal")
        self.insert(END, texto)
        self.configure(state="disable")
    def insertar_texto_concatenado(self, texto):
        """
        Inserta el texto especificado al final del texto existente en el área de texto.

        Args:
            texto (str): El texto que se añadirá al final del texto existente en el área de texto.
        """
        self.configure(state="normal")
        self.insert(END, texto + "\n")
        self.configure(state="disable")
    def mostrar_tabla(self, tabla: Tablas):
        """
        Muestra la tabla especificada en el área de texto.

        Args:
            tabla (Tablas): La tabla que se mostrará en el área de texto.
        """
        self.configure(state="normal")

        # Obtener los títulos y los datos de las columnas de la tabla
        titulos = tabla.titulos
        datos_columnas = tabla.valoresColumna

        # Transponer los datos de la tabla
        tabla_transpuesta = list(map(list, zip(*datos_columnas)))

        # Convertir la tabla a una cadena de texto con tabulate
        tabla_texto = tabulate(tabla_transpuesta, headers=titulos)

        # Insertar la tabla en el área de texto
        self.insert(END, tabla_texto)

        self.configure(state="disable")
    def insertar_lista(self, lista):
        """
        Inserta una lista de elementos como texto en el área de texto sin borrar el contenido existente.

        Args:
            lista (list): La lista de elementos que se insertarán en el área de texto.
        """
        self.configure(state="normal")

        # Convertir la lista a una cadena de texto con los elementos separados por comas
        lista_texto = ', '.join(map(str, lista))

        # Insertar la lista al final del contenido existente en el área de texto
        self.insert(END, lista_texto + "\n")

        self.configure(state="disable")


    def mostrar_tabla_sin_borrar(self, tabla: Tablas):
        """
        Inserta la tabla especificada en el área de texto sin borrar el contenido existente.

        Args:
            tabla (Tablas): La tabla que se insertará en el área de texto.
        """
        self.configure(state="normal")

        # Obtener los títulos y los datos de las columnas de la tabla
        titulos = tabla.titulos
        datos_columnas = tabla.valoresColumna

        # Transponer los datos de la tabla
        tabla_transpuesta = list(map(list, zip(*datos_columnas)))

        # Convertir la tabla a una cadena de texto con tabulate
        tabla_texto = tabulate(tabla_transpuesta, headers=titulos)

        # Insertar la tabla en el área de texto
        self.insert(END, tabla_texto + "\n")

        self.configure(state="disable")

    def insertar_salto_linea(self):
        """
        Inserta dos saltos de línea en el área de texto.
        """
        self.configure(state="normal")
        self.insert(END, "\n\n")
        self.configure(state="disable")


    def obtener_texto(self):
        """
        Obtiene todo el texto presente en el área de texto.

        Returns:
            str: El texto presente en el área de texto.
        """
        return self.get(1.0, END)
