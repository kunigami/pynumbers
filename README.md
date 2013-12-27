Python Number theory library
============================
Algorithms:

  - Greatest common divisor: <code>gdc(a, b)</code>
    - complexity: <code>O(log(min(a,b)))</code>
    - memory: <code>O(log(min(a,b)))</code>
    - description: computes the greatest common divisor between a and b

  - Modular Exponentiation: <code>modexp(base, power, mod)</code>
    - complexity: <code>O(log(power))</code>
    - memory: <code>O(log(power))</code>
    - description: computes (base^power) % mod

  - Pell's Equation: <code>pell_solutions(n, k)</code>
    - complexity: <code>O(n^(1/2) log n)</code>
    - memory: <code>O(k)</code>
    - desciption: computes a list with the first k solutions of the Pell 
                  equation: x^2 - n(y^2) = 1

  - Eratosthenes' Sieve: <code>sieve(n)</code>
    - complexity: <code>O(n (log log n))</code>
    - memory: <code>O(n)</code>
    - description: sieve of eratosthenes to find primes less than n

  - Miller Rabin Primality Test: <code>miller_rabin(n, k=10)</code>
    - complexity: <code>O(k*(log n)^3)</code>
    - memory:
    - description: find primes less than n with 4^(-k) probability
