import numpy as np


class EcDiferenciales:

    @classmethod
    def euler(cls, f, a, b, h, co):
        """
        :param f: function
        :param a: interval(first value)
        :param b: interval(second value)
        :param h: time interval
        :param co: initial condition of the function
        :return: time, approach to function
        """
        n = int((b-a)/h)
        yeu = [co]  # y_euler
        t = np.linspace(a, b, n+1)
        for i in range(n):
            yeu.append(yeu[i]+h*f(t[i], yeu[i]))
        return t, yeu

    @classmethod
    def runge_kutta_4(cls, f, a, b, h, co):
        """
        :param f: function
        :param a: interval(first value)
        :param b: interval(second value)
        :param h: time interval
        :param co: initial condition of the function
        :return: time, approach to function
        """
        n = int((b - a) / h)
        t = [a]
        yeu = [co]
        for i in range(n):
            k1 = h * f(t[i], yeu[i])
            k2 = h * f(t[i] + 0.5 * h, yeu[i] + 0.5 * k1)
            k3 = h * f(t[i] + 0.5 * h, yeu[i] + 0.5 * k2)
            k4 = h * f(t[i] + h, yeu[i] + k3)
            yeu.append(yeu[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
            t.append(t[i]+h)
        return t, yeu
