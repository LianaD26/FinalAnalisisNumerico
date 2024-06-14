import tkinter as tk
from tkinter import messagebox
from ...controllers.interpolacion_ajuste_controller import InterAjusteController


class IPolSimple:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Polinomial simple")

        self.label_x = tk.Label(self.root, text="Valores de x (separados por coma):")
        self.label_x.pack(pady=5)
        self.entry_x = tk.Entry(self.root)
        self.entry_x.pack(pady=5)

        self.label_y = tk.Label(self.root, text="Valores de y (separados por coma):")
        self.label_y.pack(pady=5)
        self.entry_y = tk.Entry(self.root)
        self.entry_y.pack(pady=5)

        self.label_aprox = tk.Label(self.root, text="Valor a aproximar:")
        self.label_aprox.pack(pady=5)
        self.entry_aprox = tk.Entry(self.root)
        self.entry_aprox.pack(pady=5)

        self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack(pady=5)

        self.root.mainloop()

    def calcular(self):
        try:
            x_str = self.entry_x.get()
            y_str = self.entry_y.get()
            x = float(self.entry_aprox.get())

            x_vals = self.validar_valores(x_str)
            y_vals = self.validar_valores(y_str)

            if len(x_vals) != len(y_vals):
                messagebox.showerror("Error", "Los conjuntos de datos deben tener la misma cantidad de valores.")
                return

            self.result_label.config(text="Datos válidos y verificados.")

            coeff = InterAjusteController.polsimple_controller(x_vals, y_vals)
            y = InterAjusteController.aprox_controller(coeff, x)

            self.result_label.config(text=f"Coeficientes: {coeff} \n"
                                          f"f({x}): {y}")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos separados por comas válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def validar_valores(self, valores_str):
        valores = valores_str.split(",")
        valores = [float(val.strip()) for val in valores if val.strip()]
        return valores
