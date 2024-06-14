import tkinter as tk
from .ceros_de_funciones.biseccion_ceros_w import IBiseccion
from .ceros_de_funciones.falsapos_ceros_w import IFalsaPos
from .ceros_de_funciones.newton_ceros_w import INewton
from .ceros_de_funciones.secante_ceros_w import ISecante


class ICeros:

    def __init__(self):
        root = tk.Tk()
        root.title("Ceros de funciones")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        btn_biseccion= tk.Button(frame, text="Bisección", command=IBiseccion)
        btn_biseccion.pack(fill=tk.X, pady=5)

        btn_falsapos = tk.Button(frame, text="Falsa posición", command=IFalsaPos)
        btn_falsapos.pack(fill=tk.X, pady=5)

        btn_newton = tk.Button(frame, text="Newton", command=INewton)
        btn_newton.pack(fill=tk.X, pady=5)

        btn_secante = tk.Button(frame, text="Secante", command=ISecante)
        btn_secante.pack(fill=tk.X, pady=5)
