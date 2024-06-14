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
        x = np.zeros(n)

        for k in range(0, n - 1):
            for i in range(k + 1, n):
                lam = A[i, k] / (A[k, k])  # lambda factor
                A[i, k:n] = A[i, k:n] - lam * A[k, k:n]  # update row
                b[i] = b[i] - lam * b[k]

        for k in range(n - 1, -1, -1):
            x[k] = (b[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / (A[k, k])

        return x

    @classmethod
    def pivoteo(cls, A, b):
        """
        This method uses pivoting to avoid zero or very small diagonal values, to ensure that
        the main diagonal element (pivot) is the maximum in its column
        :param A:
        :param b:
        :return:
        """
        n = len(b)
        for i in range(n):
            max_fila = np.argmax(np.abs(A[i:n, i])) + i
            if A[max_fila, i] == 0:
                raise ValueError("El sistema no tiene solución única.")
            A[[i, max_fila]] = A[[max_fila, i]]
            b[[i, max_fila]] = b[[max_fila, i]]
            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
                b[j] -= factor * b[i]
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
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
