# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        # Only consider odd numbers to save space
        primes = [True] * (n // 2)
        # index i represents number 2*i + 1

        for i in range(3, int(n**0.5) + 1, 2):
            if primes[i // 2]:
                # start from i*i, step by 2*i (skip even multiples)
                for j in range(i * i, n, 2 * i):
                    primes[j // 2] = False

        return sum(primes)  # counts odd primes