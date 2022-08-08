"""
    A skew binary number is a number representation in which a digit in position
    i, di, is one of [0, 1, 2], and has weight wi = 2^(i+1) - 1. The decimal
    representation of this number is given by  sum(di * wi).

    The canonical form states that no non-zero digit follows a digit 2. Which
    implies there are at most one digit 2 in the number and a 2 is followed by
    0s. It's possible to show that there's a 1:1 mapping between decimals and
    skewed binary numbers in their canonical form.

    Examples:

    0 - 0
    1 - 1
    2 - 2
    3 - 10
    4 - 11
    5 - 12
    6 - 20
    7 - 100
"""


def decimalToSkewedBinaryInner (n, weight):
    if n < weight:
        return (n, [])
    else:
        rest, skewDigits = decimalToSkewedBinaryInner(n, 2*weight + 1)
        if rest == 2*weight :
            return (0, skewDigits + [2])
        elif rest >= weight :
            return (rest - weight, skewDigits + [1])
        else:
            return (rest, skewDigits + [0])

def decimalToSkewedBinary (n):
    """
        Converts a number in decimal to a string with the skewed binary
        representation
    """
    if n == 0:
        return [0]
    remainder, digits = decimalToSkewedBinaryInner(n, 1)
    assert remainder == 0
    return digits
