# Return a list with the first k solutions of the Pell equation x^2 - n(y^2) = 1
def pell_solver(n, k):

    sols = []

    r = sqrt(n)
    a = int(r)

    p0, p1 = 1, a
    q0, q1 = 0, 1

    # Iterate over convergents until we find a solution
    while p1*p1 - n*q1*q1 != 1:
        r = 1.0 / (r - a)
        a = int(r)

        p0, p1 = p1, a*p1 + p0
        q0, q1 = q1, a*q1 + q0

    # Generate the next k-1 solutions from the fundamental one
    f = f0 = p1+q1*sqrt(n)
    g = g0 = p1-q1*sqrt(n)
    for k in range(1,k+1):
        x = int((f + g)/2 + 0.0001)
        y = int((f - g)/(2*sqrt(n)) + 0.0001)
        f *= f0
        g *= g0
        sols.append([x, y])
    return sols
