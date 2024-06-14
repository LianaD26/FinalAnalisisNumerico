import tkinter as tk
from tkinter import ttk
from ..controllers.main_controller import main_controller


def main_window():
    root = tk.Tk()
    root.config(width=300, height=200)
    root.title("Análisis numérico")
    window_width = 400
    window_height = 300
    center_window(root, window_width, window_height)
    root.update_idletasks()

    # Crear botones
    buttons = ["Serie de Taylor", "Ceros de funciones", "Sistema Ec.Lineales", "Interpolacion y ajuste",
               "Sistema Ec.Diferenciales"]
    for i, button_text in enumerate(buttons):
        button = ttk.Button(root, text=button_text, command=lambda bt=button_text: main_controller(bt))
        button.place(x=100, y=45 + i * 40)

    root.mainloop()


def center_window(window, width, height):
    # screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # adjust window geometry
    window.geometry(f'{width}x{height}+{x}+{y}')
