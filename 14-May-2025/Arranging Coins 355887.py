# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:

        low = 0
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                low = mid + 1
            else:
                high = mid - 1
        return high