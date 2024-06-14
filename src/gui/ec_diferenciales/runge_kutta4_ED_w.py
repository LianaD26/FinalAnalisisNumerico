import tkinter as tk
from tkinter import messagebox
import numpy as np
from sympy import symbols, sympify, lambdify, sin, cos, tan, pi, E
from ...controllers.ED_controller import EcDifController


class IRungeK:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Runge Kutta")

        self.count_frame = tk.Frame(self.root)
        self.count_frame.pack(pady=10)

        self.label_a = tk.Label(self.count_frame, text="a (primer valor del intervalo):")
        self.label_a.pack(pady=5)
        self.entry_a = tk.Entry(self.count_frame)
        self.entry_a.pack(pady=5)

        self.label_b = tk.Label(self.count_frame, text="b (segundo valor del intervalo):")
        self.label_b.pack(pady=5)
        self.entry_b = tk.Entry(self.count_frame)
        self.entry_b.pack(pady=5)

        self.label_h = tk.Label(self.count_frame, text="h (intervalo de tiempo):")
        self.label_h.pack(pady=5)
        self.entry_h = tk.Entry(self.count_frame)
        self.entry_h.pack(pady=5)

        self.label_count = tk.Label(self.count_frame, text="Cantidad de ecuaciones:")
        self.label_count.pack(pady=5)
        self.entry_count = tk.Entry(self.count_frame)
        self.entry_count.pack(pady=5)

        self.btn_submit_count = tk.Button(self.count_frame, text="Aceptar", command=self.mostrar_ecuaciones)
        self.btn_submit_count.pack(side=tk.LEFT, padx=5)

        # Frame for equations
        self.ecuaciones_frame = tk.Frame(self.root)
        self.ecuaciones_frame.pack(pady=10)

        # Frame for results with scrollbar
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.result_frame)
        self.scrollbar = tk.Scrollbar(self.result_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.root.mainloop()

    def mostrar_ecuaciones(self):
        try:
            self.cantidad = int(self.entry_count.get())
            if self.cantidad <= 0:
                raise ValueError

            for widget in self.ecuaciones_frame.winfo_children():
                widget.destroy()

            self.labels = []
            self.entries = []

            for i in range(self.cantidad):
                label = tk.Label(self.ecuaciones_frame, text=f"Ecuación {i + 1}:")
                label.grid(row=i, column=0, padx=5, pady=5)
                self.labels.append(label)

                entry = tk.Entry(self.ecuaciones_frame)
                entry.grid(row=i, column=1, padx=5, pady=5)
                self.entries.append(entry)

            ci_label = tk.Label(self.ecuaciones_frame, text="Condiciones iniciales (separadas por , en orden):")
            ci_label.grid(row=self.cantidad, column=0, padx=5, pady=5)
            self.entry_ci = tk.Entry(self.ecuaciones_frame)
            self.entry_ci.grid(row=self.cantidad, column=1, padx=5, pady=5)

            self.btn_procesar = tk.Button(self.ecuaciones_frame, text="Procesar", command=self.procesar_ecuaciones)
            self.btn_procesar.grid(row=self.cantidad + 1, column=0, columnspan=2, pady=10)

        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero positivo.")

    def procesar_ecuaciones(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        h = float(self.entry_h.get())
        try:
            x = symbols('x')
            ecuaciones = []
            for entry in self.entries:
                eq_str = entry.get()
                try:
                    # Intentar convertir la ecuación a un número
                    const_val = float(eq_str)
                    ecuaciones.append(const_val)
                except ValueError:
                    # Si no es un número, convertirla a expresión simbólica
                    eq_sym = sympify(eq_str, locals={'x': x, 'sin': sin, 'cos': cos, 'tan': tan, 'pi': pi, 'E': E})
                    ecuaciones.append(eq_sym)

            # Inicializar las condiciones iniciales
            ci_str = self.entry_ci.get()
            condiciones_iniciales = [float(ci) for ci in ci_str.split(',')]

            # Crear la función f_general dinámica
            def f_general(t, y):
                n = len(y)
                F = np.zeros(n)
                for i in range(len(y) - 1):
                    F[i] = y[i + 1]
                for i in range(len(y) - 1, n):
                    if isinstance(ecuaciones[i - (len(y) - 1)], (int, float)):
                        # Si es una constante, asignarla directamente
                        F[i] = ecuaciones[i - (len(y) - 1)]
                    else:
                        # Si es una expresión simbólica, evaluarla
                        F[i] = lambdify([t] + list(y), ecuaciones[i - (len(y) - 1)])(t, *y)
                return F

            print("Ecuaciones ingresadas:", ecuaciones)
            print("Condiciones iniciales:", condiciones_iniciales)

            t_values, yeu = EcDifController.rungek_controller(f_general, a, b, h, condiciones_iniciales)
            print(t_values)
            print(yeu)

            self.mostrar_resultados(t_values, yeu)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resultados(self, t_values, yeu):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Column headers
        label_t = tk.Label(self.scrollable_frame, text="Valores de t:")
        label_t.grid(row=0, column=0, padx=5, pady=5)

        label_y = tk.Label(self.scrollable_frame, text="Valores de yeu:")
        label_y.grid(row=0, column=1, padx=5, pady=5)

        # Populate data
        for i, (t, y) in enumerate(zip(t_values, yeu), start=1):
            tk.Label(self.scrollable_frame, text=str(t)).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(self.scrollable_frame, text=str(y)).grid(row=i, column=1, padx=5, pady=5)
