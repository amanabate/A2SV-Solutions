# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def get_total(div):
            total = 0
            for val in nums:
                total += (val + div - 1) // div  # You forgot the division here
            return total

        low = 1
        high = max(nums)

        while low < high:
            mid_val = (low + high) // 2
            if get_total(mid_val) > threshold:  
                low = mid_val + 1
            else:
                high = mid_val

        return low
