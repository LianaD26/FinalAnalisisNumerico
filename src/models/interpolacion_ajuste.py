import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


class InterpolacionAjuste:
    @classmethod
    def polinomial_simple(cls, x_data, y_data):
        """
        This function returns a list of coefficients that will be replaced in the polynomial
        :param x_data: values of x
        :param y_data: values of y
        :return: list of coefficients
        """
        n = len(x_data)
        M_p = np.zeros([n, n])
        for i in range(n):
            M_p[i, 0] = 1
            for j in range(1, n):
                M_p[i, j] = M_p[i, j - 1] * x_data[i]

        a_i = np.linalg.solve(M_p, y_data)
        return a_i

    @classmethod
    def pol_lagrange(cls, x_d, y_d):
        """
        This function returns a polynomial of degree n with n+1 points
        :param x_d: values of x
        :param y_d: values of y
        :return: expanded polynomial
        """
        x = sp.symbols("x")
        n = len(x_d)
        S = 0  # suma
        for i in range(n):
            pr = 1  # production
            for j in range(n):
                if j != i:
                    pr = pr * ((x - x_d[j]) / (x_d[i] - x_d[j]))  # pol lagrange * Y_i
            S = S + pr * y_d[i]
        return S.expand()

    @classmethod
    def minimos_cuadrados(cls, xd, yd):
        """
        :param xd: values of x
        :param yd: values of y
        :return: coefficients of the equation of the line
        """
        n = len(xd)
        sx = sum(xd)
        sf = sum(yd)
        sx2 = sum(x ** 2 for x in xd)
        sfx = sum(xd[i]*yd[i] for i in range(len(xd)))
        a0 = (sf * sx2 - sx * sfx) / (n * sx2 - sx ** 2)
        a1 = (n * sfx - sf * sx) / (n * sx2 - sx ** 2)
        return a0, a1

    @classmethod
    def evaluar_polinomio(cls, pol, x):
        """
        Evaluate the polynomial at a specific point
        :param pol: polynomial
        :param x: specific point
        :return: value of y at the specific point
        """
        suma = 0
        for i in range(len(pol)):
            suma = suma + pol[i] * (x ** i)
        return suma

    @classmethod
    def evaluar_polinomio_sympy(cls, pol, valor_reemplazo):
        """
        Evaluate the symbolic polynomial at a specific point
        :param pol: polynomial
        :param valor_reemplazo: specific point
        :return: value of y at the specific point
        """
        x = sp.symbols('x')
        y = pol.subs(x, valor_reemplazo)
        return y

    @classmethod
    def graficar_mod_no_lineales(cls, x_d, y_d):
        """
        Graph the functions to find a nonlinear model
        :param x_d: values of x
        :param y_d: values of y
        :return: graphics with matplotlib
        """
        plt.figure(figsize=(9, 9), dpi=80)
        plt.subplot(331)
        plt.plot(x_d, y_d, "dr", label="x")
        plt.legend()

        plt.subplot(332)
        plt.plot(x_d ** 2, y_d, "dg", label="x^2")
        plt.legend()

        plt.subplot(333)
        plt.plot(x_d ** 3, y_d, "dc", label="x^3")
        plt.legend()

        plt.subplot(334)
        plt.plot(x_d, np.sqrt(y_d), "dg", label="sqrt(y)")
        plt.legend()

        plt.subplot(335)
        plt.plot(x_d, 1 / np.sqrt(y_d), "db", label="1/sqrt(y)")
        plt.legend()

        plt.subplot(336)
        plt.plot(np.log(x_d), y_d, "dc", label="ln(x)")
        plt.legend()

        plt.subplot(337)
        plt.plot(np.log(x_d), np.log(y_d), "dg", label="ln(x) ln(y)")
        plt.legend()

        plt.subplot(338)
        plt.plot(x_d, np.log(y_d), "dr", label="ln(y)")
        plt.legend()

        plt.subplot(339)
        plt.plot(x_d, y_d ** 2, "db", label="y^2")
        plt.legend()

        plt.show()
