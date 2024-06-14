from ..models.ceros import Ceros


class CerosController:
    @classmethod
    def biseccion_controller(cls, a, b, tol, function):
        root, iterations = Ceros.bisection(a, b, tol, function)
        return root, iterations

    @classmethod
    def falsapos_controller(cls, a, b, tol, function):
        root, iterations = Ceros.posfalsa(a, b, tol, function)
        return root, iterations

    @classmethod
    def newton_controller(cls, f, x0, tol, x):
        root, iterations = Ceros.newton(f, x0, tol, x)
        return root, iterations

    @classmethod
    def secante_controller(cls, f, x0, x1, tol):
        root, iterations = Ceros.secante(f, x0, x1, tol)
        return root, iterations
