# Authors: Nikoo Sabzevar, Sara Ghandehari

from numpy.random import uniform
from Hw1_exc1 import factorial


def binomial_rv(n, p):
    """
    The binomial random variable Y∼Bin(n,p) represents the number of successes in n binary
    trials, where each trial succeeds with probability p. function bionomial_rv(n,p) finds
    number of successes in n trial, where the probability of being true in each trial is
    equal to p.

    """
    Y = int(uniform(1, n + 1))
    bn = p ** Y * (1 - p) ** (n - Y) * factorial(n) / (factorial(Y) * factorial(n - Y))
    bn = round(bn, 3)
    return [Y, bn]


import numpy as np


def bino(n, p):
    counter = 0
    for i in range(n):
        uval = np.random.uniform(0, 1)
        if uval <= p:
            counter += 1
    return counter


n = 25
p = 0.8  # number of times that coins face tail
# print(binomial_rv(n, p))
print(bino(n, p))
