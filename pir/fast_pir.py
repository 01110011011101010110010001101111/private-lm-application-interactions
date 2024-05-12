from sage.all import *

class PIR:
    def __init__(self, lhe):
        self.st = None
        self.lhe = lhe
        self.A = None
        self.q = lhe.q

    def query(self, i, j, sqrtN):
        uj = matrix(GF(2), sqrtN, [0]*sqrtN)
        uj[j] = 1

        sk = self.lhe.gen()

        qu = self.lhe.enc(uj, sk)
        
        self.st = (sk, i)

        return qu, self.st

    def answer(self, D, qu):
        A, b = qu
        ans = (matrix(GF(self.q), D) * A, matrix(GF(self.q), D) * b)

        return ans

    def reconstruct(self, ans, st):
        sk, i = st
        H, c = ans

        v = self.lhe.dec(H, c, sk)

        return v[i]

