import tkinter as tk
from .ec_diferenciales.euler_ED_w import IEuler
from .ec_diferenciales.runge_kutta4_ED_w import IRungeK


class IEcDiferenciales:
    def __init__(self):
        root = tk.Tk()
        root.title("Ecuaciones diferenciales")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        btn_euler = tk.Button(frame, text="Euler", command=IEuler)
        btn_euler.pack(fill=tk.X, pady=5)

        btn_rungek = tk.Button(frame, text="Runge Kutta 4 orden", command=IRungeK)
        btn_rungek.pack(fill=tk.X, pady=5)
