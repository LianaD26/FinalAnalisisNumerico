import tkinter as tk
from tkinter import messagebox

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, sympify, lambdify, sin, cos, tan, pi, E
from ...controllers.ceros_controller import CerosController


class ISecante:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Secante")

        self.label_a = tk.Label(self.root, text="x0:")
        self.label_a.pack(pady=5)
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack(pady=5)

        self.label_b = tk.Label(self.root, text="x1:")
        self.label_b.pack(pady=5)
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack(pady=5)

        self.label_tol = tk.Label(self.root, text="Tolerancia:")
        self.label_tol.pack(pady=5)
        self.entry_tol = tk.Entry(self.root)
        self.entry_tol.pack(pady=5)

        self.label_function = tk.Label(self.root, text="Función f(x):")
        self.label_function.pack(pady=5)
        self.entry_function = tk.Entry(self.root)
        self.entry_function.pack(pady=5)

        self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack(pady=5)

        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(pady=10)

        self.root.mainloop()

    def calcular(self):
        try:
            x0 = float(self.entry_a.get())
            x1 = float(self.entry_b.get())
            tol = float(self.entry_tol.get())
            func_str = self.entry_function.get()

            if x0 >= x1:
                messagebox.showerror("Error", "El valor de a debe ser menor que el de b.")
                return

            x = symbols('x')
            f_sym = sympify(func_str, locals={'sin': sin, 'cos': cos, 'tan': tan, 'pi': pi, 'E': E})
            f = lambdify(x, f_sym, 'numpy')

            root, iterations = CerosController.secante_controller(f, x0, x1, tol)

            self.result_label.config(text=f"El resultado es: {root} con {iterations} iteraciones")

            self.graficar(f, x0, x1)

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def graficar(self, f, x0, x1):
        # Clear previous plot if exists
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()

        x_vals = np.linspace(x0 - 1, x1 + 1, 400)
        y_vals = f(x_vals)

        ax.plot(x_vals, y_vals, label="f(x)")
        ax.axvline(x=x0, color='r', linestyle='--', label='x0')
        ax.axvline(x=x1, color='r', linestyle='--', label='x1')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
