from customtkinter import CTkButton

class JButton(CTkButton):
    """
    Clase que representa un botón personalizado utilizando la biblioteca customtkinter.

    Args:
        master: El widget padre al que pertenece este botón.
        nombre_boton (str): El texto que se mostrará en el botón.
        funcion (callable): La función que se llamará cuando se haga clic en el botón.

    Attributes:
        master: El widget padre al que pertenece este botón.
        nombre_boton (str): El texto que se mostrará en el botón.
        funcion (callable): La función que se llamará cuando se haga clic en el botón.

    """

    def __init__(self, master, nombre_boton, funcion):
        """
        Inicializa un nuevo JButton.

        Args:
            master: El widget padre al que pertenece este botón.
            nombre_boton (str): El texto que se mostrará en el botón.
            funcion (callable): La función que se llamará cuando se haga clic en el botón.

        """
        super().__init__(master=master)

        # Configura las propiedades del botón
        self.configure(command=funcion,          # La función que se ejecutará al hacer clic en el botón
                       font=("Arial", 14, "bold"),  # Fuente del texto del botón
                       text_color="#FFFFFF",      # Color del texto del botón
                       border_color="#5799da",    # Color del borde del botón
                       fg_color="#5799da",        # Color de fondo del botón
                       corner_radius=5,           # Radio de las esquinas del botón
                       text=f"{nombre_boton}",   # Texto que se mostrará en el botón
                       hover_color="#3768b7"     # Color de fondo cuando el cursor se desplaza sobre el botón
                       )
