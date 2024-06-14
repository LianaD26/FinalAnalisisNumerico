from ..models.interpolacion_ajuste import InterpolacionAjuste


class InterAjusteController:
    @classmethod
    def lagrange_controller(cls, x_d, y_d):
        # Symbolic
        return InterpolacionAjuste.pol_lagrange(x_d, y_d)

    @classmethod
    def mincuadrados_controller(cls, x_d, y_d):
        a0, a1 = InterpolacionAjuste.minimos_cuadrados(x_d, y_d)
        return a0, a1

    @classmethod
    def polsimple_controller(cls, x_d, y_d):
        # list of coefficients
        return InterpolacionAjuste.polinomial_simple(x_d, y_d)

    @classmethod
    def aprox_controller_sympy(cls, pol, x):
        return InterpolacionAjuste.evaluar_polinomio_sympy(pol, x)

    @classmethod
    def aprox_controller(cls, pol, x):
        return InterpolacionAjuste.evaluar_polinomio(pol, x)
