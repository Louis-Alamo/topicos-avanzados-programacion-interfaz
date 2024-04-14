from customtkinter import CTkLabel

class JLabel(CTkLabel):
    """
    Clase que representa una etiqueta personalizada utilizando la biblioteca customtkinter.

    Args:
        master: El widget padre al que pertenece esta etiqueta.
        texto (str): El texto que se mostrará en la etiqueta.

    Attributes:
        master: El widget padre al que pertenece esta etiqueta.
        texto (str): El texto que se muestra actualmente en la etiqueta.

    """

    def __init__(self, master, texto):
        """
        Inicializa una nueva JLabel.

        Args:
            master: El widget padre al que pertenece esta etiqueta.
            texto (str): El texto que se mostrará en la etiqueta.

        """
        super().__init__(master=master)

        # Configura las propiedades de la etiqueta
        self.configure(text=f"{texto}",     # Texto que se mostrará en la etiqueta
                       text_color="#000000",  # Color del texto en la etiqueta
                       font=("Arial", 16, "bold"),  # Fuente del texto en la etiqueta
                       bg_color="#ffffff"     # Color de fondo de la etiqueta
                       )

    def cambiar_texto(self, texto):
        """
        Cambia el texto que se muestra en la etiqueta.

        Args:
            texto (str): El nuevo texto que se mostrará en la etiqueta.
        """
        self.configure(text=f"{texto}")
