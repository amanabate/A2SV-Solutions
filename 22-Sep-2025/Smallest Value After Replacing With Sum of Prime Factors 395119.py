# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor_sum(x):
            s, d = 0, 2
            temp = x
            while d * d <= temp:
                while temp % d == 0:
                    s += d
                    temp //= d
                d += 1
            if temp > 1:
                s += temp
            return s

        prev = -1
        while n != prev:
            prev = n
            n = prime_factor_sum(n)
        return n