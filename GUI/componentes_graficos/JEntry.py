from customtkinter import CTkEntry
from tkinter import END
class JEntry(CTkEntry):
    """
    Clase que representa un campo de entrada personalizado utilizando la biblioteca customtkinter.

    Args:
        master: El widget padre al que pertenece este campo de entrada.

    Attributes:
        master: El widget padre al que pertenece este campo de entrada.

    """

    def __init__(self, master):
        """
        Inicializa un nuevo JEntry.

        Args:
            master: El widget padre al que pertenece este campo de entrada.

        """
        super().__init__(master=master)

        # Configura las propiedades del campo de entrada
        self.configure(font=("Arial", 16, "bold"),  # Fuente del texto en el campo de entrada
                       text_color="#000000",       # Color del texto en el campo de entrada
                       border_color="#77b4e3",     # Color del borde del campo de entrada
                       fg_color="#e0eef9",         # Color de fondo del campo de entrada
                       corner_radius=5             # Radio de las esquinas del campo de entrada
                       )

    def obtener_texto(self):
        """
        Obtiene el texto actualmente ingresado en el campo de entrada.

        Returns:
            str: El texto ingresado en el campo de entrada.
        """
        return self.get()

    def mostrar_texto(self, texto):
        """
        Muestra el texto especificado en el campo de entrada, reemplazando el texto existente.

        Args:
            texto (str): El texto que se mostrará en el campo de entrada.
        """
        self.eliminar_texto()
        self.insert(0, texto)

    def eliminar_texto(self):
        """
        Elimina todo el texto actualmente presente en el campo de entrada.
        """
        self.delete(0, END)
