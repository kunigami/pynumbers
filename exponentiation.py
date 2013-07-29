def modexp(base, power, mod):
    if (power == 0):
        return 1
    r = modexp(base, power/2, mod)
    r = (r*r) % mod
    if (power % 2 == 1):
        r = (r * base) % mod
    return r
