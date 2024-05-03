import numpy as np

class PIR:
    def __init__(self, fhe):
        self.st = None
        self.lhe = lhe

    def query(self, i, j, n):
        uj = np.zeros((n,))
        uj[j] = 1

        sk = self.lhe.gen(n)

        qu = self.lhe.enc(sk, uj)
        
        self.st = (sk, i)

        return qu, self.st

    def answer(self, D, qu):
        ans = D * qu

        return ans

    def reconstruct(self, ans, st):
        sk, i = self.st

        v = self.lhe.dec(sk, ans)

        return v[i]

