# Importing necessary modules from SageMath
from sage.matrix.constructor import random_matrix
from sage.modules.free_module_element import zero_vector
from sage.all import *

class Self:
    pass

self = Self()

self.q = 5
self.n = 2
self.m = 2

A = random_matrix(GF(self.q), self.m, self.n)
s = random_matrix(GF(self.q), self.n, 1)

print(A*s)

# print(zero_vector(GF(2), 2))

# # Define the base q
# q = 5
# 
# # Generate a random matrix of size 3x3 in base q
# print(random_matrix(GF(q), 3, 3))

