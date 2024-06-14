import tkinter as tk
from .interpolacion_ajuste.lagrange_interp_ajuste_w import ILagrange
from .interpolacion_ajuste.min_cuadrados_interp_ajuste_w import IMinCuadrados
from .interpolacion_ajuste.pol_simple_interp_ajuste_w import IPolSimple


class IAjuste:
    def __init__(self):
        root = tk.Tk()
        root.title("Interpolación y ajuste")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        btn_lagrange = tk.Button(frame, text="Lagrange", command=ILagrange)
        btn_lagrange.pack(fill=tk.X, pady=5)

        btn_mincuadrados = tk.Button(frame, text="Mínimos cuadrados", command=IMinCuadrados)
        btn_mincuadrados.pack(fill=tk.X, pady=5)

        btn_polsimple= tk.Button(frame, text="Polinomial simple", command=IPolSimple)
        btn_polsimple.pack(fill=tk.X, pady=5)
