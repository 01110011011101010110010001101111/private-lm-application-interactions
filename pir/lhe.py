from sage.matrix.constructor import random_matrix
from sage.modules.free_module_element import random_vector
from sage.all import *

class LHE:
    def __init__(self, q, m, n, B=1):
        """
        m x n matrix base q
        """
        self.m = m
        self.n = n
        self.q = q
        # [-B, B] error distribution
        self.B = B

    def gen(self):
        return random_matrix(GF(self.q), self.n, 1)

    def enc(self, v, s):
        A = random_matrix(GF(self.q), self.m, self.n)
        e = matrix(GF(self.q), self.m, 1, lambda i, j: randint(-self.B, self.B))
        return (A, A * s + e + int(self.q / 2) * matrix(GF(self.q), v))

    def dec(self, A, b, s):
        c = b - A * s

        # round each entry to the nearest multiple of q/2 and divide by q/2
        c = matrix(GF(2), c.nrows(), c.ncols(), [[round(int(c[i, j]) / int(self.q/2)) for j in range(c.ncols())] for i in range(c.nrows())])

        return c
