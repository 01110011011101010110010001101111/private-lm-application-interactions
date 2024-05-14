from pir import PIR
from lhe import LHE
from sage.all import *

q = 11
m = n = 2
N = 4
sqrtN = 2

lhe = LHE(q, m, n)
pir = PIR(lhe)

D = [[1, 0], [0, 1]]

def query_with_pir(i, j):
    qu, st = (pir.query(i, j, sqrtN))
    return (pir.reconstruct(pir.answer(matrix(GF(2), 2, 2, D), qu), st))[0]

assert query_with_pir(0, 0) == 1
assert query_with_pir(0, 1) == 0
assert query_with_pir(1, 0) == 0
assert query_with_pir(1, 1) == 1
