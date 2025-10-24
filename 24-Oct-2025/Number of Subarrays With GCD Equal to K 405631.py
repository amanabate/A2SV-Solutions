# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

from math import gcd

class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_gcd = 0
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1
                elif current_gcd < k:
                    # If GCD drops below k, it cannot reach k by adding more elements
                    break
        
        return count
