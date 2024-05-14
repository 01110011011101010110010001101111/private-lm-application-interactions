from lhe import LHE
from sage.all import *

lhe = LHE(11, 2, 2)
sk = lhe.gen()

A, b = lhe.enc(matrix(GF(2), [[0], [0]]), sk)
assert(lhe.dec(A, b, sk)[0][0] == 0)
assert(lhe.dec(A, b, sk)[1][0] == 0)

A, b = lhe.enc(matrix(GF(2), [[1], [0]]), sk)
pt = lhe.dec(A, b, sk)
assert(lhe.dec(A, b, sk)[0][0] == 1)
assert(lhe.dec(A, b, sk)[1][0] == 0)

A, b = lhe.enc(matrix(GF(2), [[0], [1]]), sk)
assert(lhe.dec(A, b, sk)[0][0] == 0)
assert(lhe.dec(A, b, sk)[1][0] == 1)

A, b = lhe.enc(matrix(GF(2), [[1], [1]]), sk)
assert(lhe.dec(A, b, sk)[0][0] == 1)
assert(lhe.dec(A, b, sk)[1][0] == 1)


