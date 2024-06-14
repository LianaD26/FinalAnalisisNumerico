import sympy as sp


class Ceros:
    @classmethod
    def bisection(cls, a, b, tol, function, i=0):
        """
        This method receives an interval of values where we will find the root
        :param a: interval(first value)
        :param b: interval(second value)
        :param tol: tolerance
        :param function: f(x)
        :param i: iterations
        :return: root, iterations
        """
        while True:
            c = (a + b) / 2
            Ea = abs(b - a)
            if Ea < tol:
                return c, i
            if function(a) * function(c) < 0:
                b = c
            else:
                a = c
            i += 1

    @classmethod
    def posfalsa(cls, a, b, tol, function, i=0):
        """
        This method receives an interval of values where we will find the root
        :param a: interval(first value)
        :param b: interval(second value)
        :param tol: tolerance
        :param function: f(x)
        :param i: iterations
        :return: root, iterations
        """
        while True:
            c = a - function(a) * (a - b) / (function(a) - function(b))

            if abs(function(c)) < tol:
                return c, i
            if function(a) * function(c) < 0:
                b = c
            else:
                a = c
            i += 1

    @classmethod
    def newton(cls, f, x0, tol, x, i=0):
        """
        Note: This method receives a symbolic function(sympy)
        :param f: function
        :param x0: initial value
        :param tol: tolerance
        :param i: iterations
        :return: root, iterations
        """
        df = sp.diff(f, x)  # primera derivada
        newT = x - f / df
        newT = sp.lambdify(x, newT)
        x1 = newT(x0)

        while abs(x1 - x0) > tol:
            x0 = x1
            x1 = newT(x0)
            i += 1
            if abs(x1 - x0) < tol:
                break

        return x1, i

    @classmethod
    def secante(cls, f, x0, x1, tol, i=0):
        """

        :param f: function
        :param x0: first seed value
        :param x1: second seed value
        :param tol: tolerance
        :param i: iterations
        :return: root, iterations
        """
        x2 = 0
        while abs(x1 - x0) > tol:
            x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
            x0 = x1
            x1 = x2
            i += 1
        return x2, i
