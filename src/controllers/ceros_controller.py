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
    def newton_controller(cls):
        pass

    @classmethod
    def secante_controller(cls):
        pass
