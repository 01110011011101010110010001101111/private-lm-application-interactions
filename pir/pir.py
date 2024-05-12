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

        A, qu = self.lhe.enc(uj, sk)
        self.A = A
        
        self.st = (sk, i)

        return qu, self.st

    def answer(self, D, qu):
        ans = matrix(GF(self.q), D) * qu

        return ans

    def reconstruct(self, ans, st):
        sk, i = self.st

        v = self.lhe.dec(self.A, ans, sk)

        return v[i]

