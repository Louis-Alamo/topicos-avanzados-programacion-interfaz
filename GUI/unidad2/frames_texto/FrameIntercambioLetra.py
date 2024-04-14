# Importaciones de librerías de Python
from tkinter import  messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JTextBox import JTextBox
from logic.textos.IntercambioLetra import IntercambioLetra
from excepciones.EmptyFieldException import EmptyFieldException

class FrameIntercambioLetra(Frame):
    """
    Clase que representa un marco para realizar el intercambio de letras en un texto.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar un texto y una letra,
    y luego realiza el intercambio de todas las vocales del texto por la letra ingresada.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameIntercambioLetra.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        titulo_frame = JLabel(self, texto="Intercambio letra")
        titulo_frame.configure(font=("Arial", 24, "bold"))
        titulo_frame.pack(pady=20,padx=20,fill=X, expand=True)

        # Campo para ingresar la letra nueva
        self.campo = CampoConTitulo(self, texto="Ingresa la letra nueva: ")
        self.campo.pack(padx=20, pady=10, expand=True, fill=X)

        # Contenedor para etiquetas de texto nuevo y texto a ingresar
        contenedor_etiquetas = Frame(self,bg="#FFFFFF")
        contenedor_etiquetas.pack(padx=20, pady=10, expand=True, fill=X)

        # Etiqueta para texto nuevo
        etiqueta_texto_nuevo = JLabel(contenedor_etiquetas, texto="Texto nuevo: ")
        etiqueta_texto_nuevo.pack(side='right' , expand=True, fill=X)

        # Etiqueta para texto a ingresar
        etiqueta_texto_antiguo = JLabel(contenedor_etiquetas, texto="Texto a ingresar: ")
        etiqueta_texto_antiguo.pack(side='left', expand=True, fill=X)

        # Contenedor para área de texto de texto antiguo y nuevo
        contenedor_area_texto = Frame(self, bg="#FFFFFF")
        contenedor_area_texto.pack(padx=20, pady=10, expand=True, fill=X)

        # Área de texto para texto antiguo
        self.area_texto_antiguo =JTextBox(contenedor_area_texto)
        self.area_texto_antiguo.pack(side='left',padx=5, expand=True, fill=BOTH)

        # Área de texto para texto nuevo
        self.area_texto_nuevo = JTextBox(contenedor_area_texto)
        self.area_texto_nuevo.pack(side='right',expand=True, fill=BOTH)

        # Botón para procesar el intercambio de letras
        boton = JButton(self, nombre_boton="Procesar", funcion=lambda: self._procesar())
        boton.pack(padx=20, pady=10, expand=True, fill=X)

    def _procesar(self):
        """
        Procesa el intercambio de letras en el texto y muestra el resultado en el área de texto.
        """
        try:
            # Obtiene el texto y la letra ingresados por el usuario
            texto = self.area_texto_antiguo.obtener_texto()
            letra = self.campo.obtener_texto()

            # Verifica si hay campos vacíos
            if texto == "" or letra == "":
                raise EmptyFieldException()

            # Realiza el intercambio de letras en el texto
            texto_nuevo = IntercambioLetra().intercambio_letra_vocales(letraNueva=letra, texto=texto)

            # Muestra el texto resultante en el área de texto nuevo
            self.area_texto_nuevo.insertar_texto(texto_nuevo)

        except EmptyFieldException:
            # Muestra un mensaje de advertencia si hay campos vacíos
            messagebox.showwarning("EmptyFieldError", "No se permiten campos vacíos.")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
