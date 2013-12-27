Python Number theory library
============================
Algorithms:
  - gdc(a, b)
    - complexity: O(log(min(a,b)))
    - memory: O(log(min(a,b)))
    - description: computes the greatest common divisor between a and b

  - pell_solutions(n, k)
    - complexity: O(n^(1/2) log n)
    - memory: O(k)
    - desciption: computes a list with the first k solutions of the Pell 
                  equation: x^2 - n(y^2) = 1

  - sieve(n)
    - complexity: O(n (log log n))
    - memory: O(n)
    - description: sieve of eratosthenes to find primes less than n