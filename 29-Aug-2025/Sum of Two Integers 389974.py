# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            if b > 0:
                a = -~a    # increment a
                b = ~-b    # decrement b
            else:
                a = ~-a    # decrement a
                b = -~b    # increment b
        return a