# Return the greatest common divisor between two numbers
def gcd(a, b):
    return gcd(b, a%b) if b > 0 else a;
