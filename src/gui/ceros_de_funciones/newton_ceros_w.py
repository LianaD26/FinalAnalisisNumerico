import tkinter as tk
from tkinter import messagebox

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, sympify, lambdify, sin, cos, tan, pi, E
from ...controllers.ceros_controller import CerosController


class INewton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Newton")

        self.label_a = tk.Label(self.root, text="x0:")
        self.label_a.pack(pady=5)
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack(pady=5)

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
            tol = float(self.entry_tol.get())
            func_str = self.entry_function.get()

            x = symbols('x')
            f_sym = sympify(func_str, locals={'sin': sin, 'cos': cos, 'tan': tan, 'pi': pi, 'E': E})
            root, iterations = CerosController.newton_controller(f_sym, x0, tol, x)
            self.result_label.config(text=f"El resultado es: {root} con {iterations} iteraciones")

            f = lambdify(x, f_sym, 'numpy')
            self.graficar(f, x0)

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def graficar(self, f, x0):
        # Clear previous plot if exists
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()

        x_vals = np.linspace(0, 100, 400)
        y_vals = f(x_vals)

        ax.plot(x_vals, y_vals, label="f(x)")
        ax.axvline(x=x0, color='r', linestyle='--', label='x0')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
