import tkinter as tk
from .sist_ecuaciones_lineales.directos.eliminacion_SEL_w import IEliminacionG
from .sist_ecuaciones_lineales.directos.pivoteo_SEL_w import IPivoteo
from .sist_ecuaciones_lineales.iterativos.gauss_seidel_matrix_SEL_w import IGaussS


class IEcLineales:
    def __init__(self):
        root = tk.Tk()
        root.title("Sistema de Ecuaciones Lineales")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        btn_gauss_seidel = tk.Button(frame, text="Gauss-Seidel", command=IGaussS)
        btn_gauss_seidel.pack(fill=tk.X, pady=5)

        btn_pivoteo = tk.Button(frame, text="Pivoteo", command=IPivoteo)
        btn_pivoteo.pack(fill=tk.X, pady=5)

        btn_eliminacion_gaussiana = tk.Button(frame, text="Eliminación Gaussiana",
                                              command=IEliminacionG)
        btn_eliminacion_gaussiana.pack(fill=tk.X, pady=5)
