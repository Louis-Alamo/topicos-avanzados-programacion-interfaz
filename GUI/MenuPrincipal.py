from tkinter import *
from customtkinter import *
from GUI.componentes_graficos.JLabel import JLabel
import sys
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameDivision import FrameDividir
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameMultiplicacion import FrameMultiplicacion
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameSuma import FrameSuma
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameResta import FrameResta

from GUI.unidad2.frame_matematicas.FramesNumericos.FramePotencias import FramePotencias
from GUI.unidad2.frame_matematicas.FramesNumericos.FrameUlam import FrameUlam
from GUI.unidad2.frame_matematicas.FramesNumericos.FrameFibonaci import FrameFibonacci


from GUI.unidad2.frame_matematicas.FramesNumericos.frames_operaciones_primos.FrameFormulaPrimos import FrameFormulaPrimos
from GUI.unidad2.frame_matematicas.FramesNumericos.frames_operaciones_primos.FrameCribaHeratostenes import FrameCribaHeratostenes
from GUI.unidad2.frame_matematicas.FramesNumericos.frames_operaciones_primos.FrameSerieNumerosNoPrimos import FrameSerieNumerosNoPrimos
from GUI.unidad2.frame_matematicas.FramesNumericos.frames_operaciones_primos.FrameGenerarNumerosPrimos import FrameGenerarNumerosPrimos

from GUI.unidad2.frames_texto.FramePalindromo import FramePalindromo
from GUI.unidad2.frames_texto.FrameIntercambioLetra import FrameIntercambioLetra

from GUI.unidad2.FrameEvaluacion.FrameEvaluacion import FrameEvaluacion

class MenuPrincipal():

    def __init__(self):

        self._ventana_principal = Tk()
        self._ventana_principal.title("Topicos avanzados de programacion")
        self._ventana_principal.config(bg="#ffffff")
        #self._ventana_principal.geometry("500x400")

        self.contenedor = CTkFrame(self._ventana_principal, fg_color="#ffffff", border_color="#77b4e3", corner_radius=10, border_width=2)
        self.contenedor.pack(padx=10,pady=10, expand=True, fill=BOTH)


        self._etiqueta = JLabel(self.contenedor, texto="Se supone que habia algo aqui :( ...")
        self._etiqueta.configure(font=("Arial", 24, "bold"))
        self._etiqueta.pack(padx=10, pady=10, expand=True, fill=BOTH)

        self._menu_bar = Menu(self._ventana_principal)

        #Creacion del todo menu de matematicas
        self._menu_matematicas = Menu(self._menu_bar, tearoff=0)


        #Creacion del menu evaluacion
        self._menu_evaluacion = Menu(self._menu_bar, tearoff=0)
        self._menu_evaluacion.add_command(label="Evaluacion", command=lambda: self._evaluacion())

        #Creacion del submenu aritmetica
        self._menu_aritmetica = Menu(self._menu_matematicas, tearoff=0)
        self._menu_aritmetica.add_command(label="Division", command=lambda: self._division())
        self._menu_aritmetica.add_command(label="Multiplicacion", command=lambda: self._multiplicacion())
        self._menu_aritmetica.add_command(label="Suma", command=lambda: self._suma())
        self._menu_aritmetica.add_command(label="Resta", command=lambda: self._resta())
        self._menu_matematicas.add_cascade(label="Aritmetica", menu=self._menu_aritmetica)


        #Creacion del submenu de numericos
        self._menu_numericos = Menu(self._menu_matematicas, tearoff=0)
        self._menu_numericos.add_command(label="Fibonaci", command=lambda: self._fibonaci())
        self._menu_numericos.add_command(label="Potencias", command=lambda: self._potencias())
        self._menu_numericos.add_command(label="Ulam", command=lambda: self._ulam())
        self._menu_matematicas.add_cascade(label="Numericos", menu=self._menu_numericos)

        #Creacion del submenu primos
        self._menu_primos = Menu(self._menu_matematicas, tearoff=0)
        self._menu_primos.add_command(label="Formula primos", command=lambda: self._formula_primos())
        self._menu_primos.add_command(label="Criba de Heratostenes", command=lambda: self._criba_de_heratostenes())
        self._menu_primos.add_command(label="Generar numeros primos", command=lambda: self._generar_numeros_primos())
        self._menu_primos.add_command(label="Serie numeros no primos", command=lambda: self._serie_numeros_no_primos())
        self._menu_matematicas.add_cascade(label="Primos", menu=self._menu_primos)


        self._menu_textos = Menu(self._menu_bar, tearoff=0)
        self._menu_textos.add_command(label="Palindromo", command=lambda: self._palindromo())
        self._menu_textos.add_command(label="Intercambio letra", command=lambda: self._intercambio_letra())

        self._menu_opciones = Menu(self._menu_bar, tearoff=0)
        self._menu_opciones.add_command(label="Reiniciar ventana", command=lambda: self._reiniciar_ventana(value=1))
        self._menu_opciones.add_command(label="Salir", command=lambda: self._salir())


        self._menu_bar.add_cascade(label="Matematicas" , menu=self._menu_matematicas)
        self._menu_bar.add_cascade(label="Textos" , menu=self._menu_textos)
        self._menu_bar.add_cascade(label="Evaluacion" , menu=self._menu_evaluacion)
        self._menu_bar.add_cascade(label="Opciones", menu=self._menu_opciones)

        self._ventana_principal.config(menu=self._menu_bar)

        self._ventana_principal.mainloop()


    def _evaluacion(self):
        self._reiniciar_ventana()
        obj = FrameEvaluacion(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _reiniciar_ventana(self, value=0):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        if value == 1:
            self._etiqueta = JLabel(self.contenedor, texto="Se supone que habia algo aqui :( ...")
            self._etiqueta.configure(font=("Arial", 24, "bold"))
            self._etiqueta.pack(padx=10, pady=10, expand=True, fill=BOTH)

    def _salir(self):
        sys.exit(0)

    #Funciones paquete matematicas

    #aritmetica
    def _division(self):
        self._reiniciar_ventana()
        obj = FrameDividir(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _multiplicacion(self):
        self._reiniciar_ventana()
        obj = FrameMultiplicacion(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _suma(self):
        self._reiniciar_ventana()
        obj = FrameSuma(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _resta(self):
        self._reiniciar_ventana()
        obj = FrameResta(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _geometria(self):
        pass


    #Numericos

    def _fibonaci(self):
        self._reiniciar_ventana()
        obj = FrameFibonacci(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _potencias(self):
        self._reiniciar_ventana()
        obj = FramePotencias(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _ulam(self):
        self._reiniciar_ventana()
        obj = FrameUlam(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)


    def _formula_primos(self):
        self._reiniciar_ventana()
        obj = FrameFormulaPrimos(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _criba_de_heratostenes(self):
        self._reiniciar_ventana()
        obj = FrameCribaHeratostenes(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _generar_numeros_primos(self):
        self._reiniciar_ventana()
        obj = FrameGenerarNumerosPrimos(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _serie_numeros_no_primos(self):
        self._reiniciar_ventana()
        obj = FrameSerieNumerosNoPrimos(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)


    #Funciones textos

    def _intercambio_letra(self):
        self._reiniciar_ventana()
        obj = FrameIntercambioLetra(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)

    def _palindromo(self):
        self._reiniciar_ventana()
        obj = FramePalindromo(self.contenedor)
        obj.pack(padx=20, pady=20,expand=True, fill=BOTH)


