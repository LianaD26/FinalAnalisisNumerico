import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from ..models.taylor import SerieTaylor


class TaylorController:
    def __init__(self):
        self.x = sp.symbols('x')

    def encontrar_polinomio(self, funcion, x0, grado):
        polinomio = SerieTaylor.s_taylor(funcion, x0, grado)
        return funcion, polinomio, self.x

    def encontrar_cota(self, f, x0, x, n):
        return SerieTaylor.cota(f, x0, x, n)
