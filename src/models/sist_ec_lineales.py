import numpy as np


class EcLineales:

    @classmethod
    def eliminacion_gaussiana(cls, A, b):
        """
        This method does not use pivoting to avoid zero or very small diagonal values
        :param A: coefficients
        :param b: matrix of b values
        :return: vector of xi values
        """
        n = len(b)
        x = [0] * n

        for k in range(n - 1):
            for i in range(k + 1, n):
                lam = A[i][k] / A[k][k]  # lambda factor
                A[i][k:n] = [A[i][j] - lam * A[k][j] for j in range(k, n)]
                b[i] -= lam * b[k]

        for k in range(n - 1, -1, -1):
            x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k + 1, n))) / A[k][k]

        return x

    @classmethod
    def pivoteo(cls, A, b):
        """
        This method uses pivoting to avoid zero or very small diagonal values, to ensure that
        the main diagonal element (pivot) is the maximum in its column
        :param A: coefficients
        :param b: matrix of b values
        :return: vector of xi values
        """
        n = len(b)

        for k in range(n - 1):
            max_index = max(range(k, n), key=lambda i: abs(A[i][k]))

            if A[max_index][k] == 0:
                raise ValueError("El método no converge a la solución del sistema.")

            if max_index != k:
                A[k], A[max_index] = A[max_index], A[k]
                b[k], b[max_index] = b[max_index], b[k]

            for i in range(k + 1, n):
                lam = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= lam * A[k][j]
                b[i] -= lam * b[k]

        x = [0] * n
        for k in range(n - 1, -1, -1):
            x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k + 1, n))) / A[k][k]

        return x

    @classmethod
    def gauss_seidel(cls, A, b, x0, tol):
        """
        :param A: coefficients
        :param b: matrix of b values
        :param x0: vector x0(values of xi in k=0)
        :param tol: tolerance
        :return: values of xi(array), spectral radius, iterations, error
        """
        D = np.diag(np.diag(A))  # diagonal
        L = D - np.tril(A)  # additive inverse of the lower diagonal
        U = D - np.triu(A)  # additive inverse of the upper diagonal
        Tg = np.dot(np.linalg.inv(D - L), U)
        Cg = np.dot(np.linalg.inv(D - L), b)
        lam, vec = np.linalg.eig(Tg)
        radio = max(abs(lam))
        i = 0  # iterations
        if radio < 1:
            x1 = np.dot(Tg, x0) + Cg
            i += 1
            while max(np.abs(x1 - x0)) > tol:
                x0 = x1
                x1 = np.dot(Tg, x0) + Cg
                i += 1
            return x1, radio, i
        else:
            print("El sistema iterativo no converge a la solución única del sistema")
