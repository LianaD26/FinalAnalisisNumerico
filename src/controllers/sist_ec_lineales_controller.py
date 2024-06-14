import numpy as np
from ..models.sist_ec_lineales import EcLineales


class EcLinealesController:
    def __init__(self):
        pass

    @classmethod
    def gauss_seidel_controller(cls, A, b, tol):
        x0 = np.zeros(len(b))
        x1, radio, i = EcLineales.gauss_seidel(A, b, x0, tol)
        return x1, radio, i
