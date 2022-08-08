from mod_exp import mod_exp
def mod_division(a, b, p):
  """
    Compute a / b % p, where p is prime.
    Undefined if p is not prime
  """
  if b % p == 0:
    raise ZeroDivisionError("division by 0")

  # modular inverse, i.e. b * inv = 1 mod p
  inv = mod_exp(b, p - 2, p)
  return ((a % p) * inv) % p
