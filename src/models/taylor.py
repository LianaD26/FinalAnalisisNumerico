import sympy as sp
import numpy as np
from math import factorial


class SerieTaylor:

    @classmethod
    def s_taylor(cls, f, x0, n):
        """
        :param f: function
        :param x0: surrounding point which constructs the polynomial
        :param n: polynomial degree
        :return: symbolic polynomial
        """
        x = sp.symbols('x')
        P = 0
        for k in range(n+1):
            df = sp.diff(f, x, k)
            dfxo = df.subs(x, x0)
            P = P+dfxo*(x-x0)**k/factorial(k)
        return P

    @classmethod
    def cota(cls, f, x0, x, n):
        """
        Calculates the maximum absolute value of the (n+1)th derivative in the interval [m, M]
        :param f: The function to be approximated(symbolic)
        :param x0: surrounding point which constructs the polynomial
        :param x: The point at which the truncation error bound is evaluated
        :param n: polynomial degree
        :return:
        """
        m = min(x0, x)
        M = max(x0, x)
        u = np.linspace(m, M, 500)
        df = sp.diff(f, x, n+1)
        df = sp.lambdify(x, df)
        Mc = np.max(np.abs(df(u)))

        return Mc*np.abs((x-x0)**(n+1)/factorial(n+1))
