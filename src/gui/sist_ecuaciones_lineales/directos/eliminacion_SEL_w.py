import tkinter as tk
from tkinter import messagebox
from ....controllers.sist_ec_lineales_controller import EcLinealesController


class IEliminacionG:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interfaz Eliminación gaussiana")

        self.coeficientes = []

        self.label_ecuaciones = tk.Label(self.root, text="Cantidad de ecuaciones:")
        self.label_ecuaciones.pack(pady=5)

        self.entry_ecuaciones = tk.Entry(self.root)
        self.entry_ecuaciones.pack(pady=5)

        self.label_variables = tk.Label(self.root, text="Cantidad de variables:")
        self.label_variables.pack(pady=5)

        self.entry_variables = tk.Entry(self.root)
        self.entry_variables.pack(pady=5)

        self.btn_mostrar_labels = tk.Button(self.root, text="Mostrar etiquetas", command=self.mostrar_etiquetas)
        self.btn_mostrar_labels.pack(pady=10)

    def mostrar_etiquetas(self):
        try:
            num_ecuaciones = int(self.entry_ecuaciones.get())
            num_variables = int(self.entry_variables.get())

            # Limpiar widgets previos
            for widget in self.root.winfo_children():
                widget.pack_forget()

            self.coeficientes = []  # Restart coefficients

            for i in range(num_ecuaciones):
                frame_ecuacion = tk.Frame(self.root)
                frame_ecuacion.pack(pady=10, padx=10, anchor=tk.W)

                ecuacion_label = tk.Label(frame_ecuacion, text=f"Ecuación {i + 1}:")
                ecuacion_label.pack()

                coeficientes_ecuacion = []
                for j in range(num_variables+1):
                    if j == num_variables:
                        var_label = tk.Label(frame_ecuacion, text=f"b:")
                        var_label.pack(side=tk.LEFT, padx=5)
                    else:
                        var_label = tk.Label(frame_ecuacion, text=f"x {j + 1}:")
                        var_label.pack(side=tk.LEFT, padx=5)
                    coeficientes_ecuacion.append(tk.Entry(frame_ecuacion))
                    coeficientes_ecuacion[-1].pack(side=tk.LEFT)

                self.coeficientes.append(coeficientes_ecuacion)

            btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
            btn_calcular.pack(pady=10)

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

    def calcular(self):
        A = []
        b = []
        for i, ecuacion in enumerate(self.coeficientes):
            # coefficients for every equation
            coeficientes = [entry.get() for entry in ecuacion]
            A_i = []
            for coef in range(len(coeficientes)):
                if coef == len(coeficientes)-1:
                    b.append(float(coeficientes[coef]))
                else:
                    A_i.append(float(coeficientes[coef]))
            A.append(A_i)
        x = EcLinealesController.eliminacion_g_controller(A, b)

        for i, ecuacion in enumerate(self.coeficientes):
            resultado_label = tk.Label(ecuacion[-1].master, text=f"Resultado x{i + 1}: {x[i]}")
            resultado_label.pack(side=tk.LEFT, padx=5)





