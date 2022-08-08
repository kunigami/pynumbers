def mod_exp(base, power, mod):
    if (power == 0):
        return 1
    r = mod_exp(base, power/2, mod)
    r = (r*r) % mod
    if (power % 2 == 1):
        r = (r * base) % mod
    return r
