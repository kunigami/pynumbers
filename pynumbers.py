################################################################################
# Number theory library in python
#
# Author: Guilherme Kunigami
################################################################################

from math import sqrt

# Return the greatest common divisor between two numbers
def gcd(a, b):
    return gcd(b, a%b) if b > 0 else a;

# Return a list with the first k solutions of the Pell equation x^2 - n(y^2) = 1
def pell_solutions(n, k):

    sols = []

    r = sqrt(n)
    a = int(r)

    p0, p1 = 1, a
    q0, q1 = 0, 1

    # Iterate over convergents until we find a solution
    while p0*p0 - n*q0*q0 != 1:
        r = 1.0 / (r - a)
        a = int(r)

        p0, p1 = p1, a*p1 + p0
        q0, q1 = q1, a*q1 + q0

    # Generate the next k-1 solutions from the fundamental one
    sols.append([p0, q0])
    for k in range(2,k):
        x = int(((p0+q0*sqrt(n))**k + (p0-q0*sqrt(n))**k)/2 + 0.0001)
        y = int(((p0+q0*sqrt(n))**k - (p0-q0*sqrt(n))**k)/(2*sqrt(n)) + 0.0001)
        sols.append([x, y])
    return sols

