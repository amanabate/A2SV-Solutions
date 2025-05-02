# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        # 5 -> no of even 0 - 9 -> "0", "2", "4", "6", "8"
        # 4 -> no of prime 0 - 9 -> "2", "3", "5", "7"

        return pow(5, even_positions, mod) * pow(4, odd_positions, mod) % mod