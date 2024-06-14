from ..models.ED import EcDiferenciales


class EcDifController:
    @classmethod
    def euler_controller(cls, f, a, b, h, co):
        t, yeu = EcDiferenciales.euler(f, a, b, h, co)
        return t, yeu

    @classmethod
    def rungek_controller(cls, f, a, b, h, co):
        t, yeu = EcDiferenciales.runge_kutta_4(f, a, b, h, co)
        return t, yeu
