Python Number theory library
============================
Algorithms:
  - <code>gdc(a, b)</code>
    - complexity: <code>O(log(min(a,b)))</code>
    - memory: <code>O(log(min(a,b)))</code>
    - description: computes the greatest common divisor between a and b

  - <code>pell_solutions(n, k)</code>
    - complexity: <code>O(n^(1/2) log n)</code>
    - memory: <code>O(k)</code>
    - desciption: computes a list with the first k solutions of the Pell 
                  equation: x^2 - n(y^2) = 1

  - <code>sieve(n)</code>
    - complexity: <code>O(n (log log n))</code>
    - memory: <code>O(n)</code>
    - description: sieve of eratosthenes to find primes less than n
