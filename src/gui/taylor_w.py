import tkinter as tk
from tkinter import messagebox
import sympy as sp
from sympy import sin, cos, tan, pi, E
from ..controllers.taylor_controller import TaylorController
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ITaylor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Polinomio de Taylor")

        self.label_funcion = tk.Label(self, text="Función:")
        self.label_funcion.grid(row=0, column=0, padx=10, pady=10)

        self.entry_funcion = tk.Entry(self)
        self.entry_funcion.grid(row=0, column=1, padx=10, pady=10)

        self.label_grado = tk.Label(self, text="Grado del Polinomio:")
        self.label_grado.grid(row=1, column=0, padx=10, pady=10)

        self.entry_grado = tk.Entry(self)
        self.entry_grado.grid(row=1, column=1, padx=10, pady=10)

        self.label_x0 = tk.Label(self, text="x0:")
        self.label_x0.grid(row=2, column=0, padx=10, pady=10)

        self.entry_x0 = tk.Entry(self)
        self.entry_x0.grid(row=2, column=1, padx=10, pady=10)

        self.label_cota_opc = tk.Label(self, text="cota:")
        self.label_cota_opc.grid(row=3, column=0, padx=10, pady=10)

        self.entry_cota_opc = tk.Entry(self)
        self.entry_cota_opc.grid(row=3, column=1, padx=10, pady=10)

        self.boton_calcular = tk.Button(self, text="Encontrar Polinomio", command=self.encontrar_polinomio)
        self.boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_cota = tk.Label(self, text="")
        self.label_cota.grid(row=6, column=0, columnspan=2, pady=10)

        self.frame_grafica = tk.Frame(self)
        self.frame_grafica.grid(row=8, columnspan=2, pady=10, padx=10)

        self.canvas = None

        self.taylor_controller = TaylorController()

    def encontrar_polinomio(self):
        funcion_str = self.entry_funcion.get()
        grado= self.entry_grado.get()
        x0 = self.entry_x0.get()
        cota_opc = self.entry_cota_opc.get()

        try:
            funcion_ = sp.sympify(funcion_str, locals={'sin': sin, 'cos': cos, 'tan': tan, 'pi': pi, 'E': E})
            grado_ = int(grado)
            x0_ = float(x0)  # Convierte usando SymPy
        except Exception as e:
            messagebox.showerror("Error", f"Error en la entrada: {e}")
            return

        funcion, polinomio, self.x = self.taylor_controller.encontrar_polinomio(funcion_, x0_, grado_)

        self.label_resultado.config(text=f"Polinomio de Taylor: {polinomio}")
        if cota_opc != '':
            cota_opc_ = float(cota_opc)
            cota = self.taylor_controller.encontrar_cota(funcion_, x0_, cota_opc_, grado_)
            self.label_cota.config(text=f"Cota en {cota_opc}: {cota}")
        else:
            self.label_cota.config(text=" ")
        self.graficar_taylor(funcion_, polinomio, x0_)

    def graficar_taylor(self, original_func, taylor_poly, x0):
        fig, ax = plt.subplots()

        p = sp.lambdify(self.x, taylor_poly)
        w = np.linspace(x0 - 1, x0 + 1, 1000)

        ax.plot(w, p(w), 'r--', label=f'Polinomio de Taylor (grado {self.entry_grado.get()})')

        original_func_lambdified = sp.lambdify(self.x, original_func)
        ax.plot(w, original_func_lambdified(w), label='Función Original')

        # Graficar el punto inicial
        ax.plot([x0], [original_func_lambdified(x0)], 'bo', label=f'Punto inicial (x0={x0})')

        ax.legend()

        for widget in self.frame_grafica.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack()
